from domain.student import Student
import random

from exceptii.eroare_repo import EroareRepo


class ServiceStudenti:

    def __init__(self,repo_studenti,validator_student):
        self.__repo_studenti = repo_studenti
        self.__validator_student = validator_student

    def adauga_student(self,id_student,nume,grup):
        student = Student(id_student,nume,grup)
        self.__validator_student.valideaza_student(student)
        self.__repo_studenti.adauga_student(student)

    def sterge_student(self,id_student):
        self.__repo_studenti.sterge_student(id_student)

    def actualizeaza_student(self,id_student,id_nou,nume_nou,grup_nou):
        student_nou = Student(id_nou,nume_nou,grup_nou)
        self.__validator_student.valideaza_student(student_nou)
        self.__repo_studenti.actualizeaza_student(id_student,id_nou,nume_nou,grup_nou)

    def get_repo(self):
        return self.__repo_studenti

    def get_student_dupa_id(self,id_student):
        return self.__repo_studenti.get_student_dupa_id(id_student)

    def nume_random(self, lungime=None):
        """
        Genereaza un nume random recursiv.
        """
        if lungime is None:
            lungime = random.randint(3, 8)
        if lungime == 0:
            return ""
        litere = "abcdefghijklmnopqrstuvwxyz"
        litera_curenta = random.choice(litere)

        return litera_curenta + self.nume_random(lungime - 1)

    def genereaza_studenti_random(self, n):
        generati = 0
        while generati < n:
            id_student = random.randint(1, 999)
            nume = self.nume_random()
            grup = random.randint(1, 999)
            student = Student(id_student, nume, grup)
            try:
                self.__repo_studenti.adauga_student(student)
                generati += 1
            except EroareRepo:
                continue