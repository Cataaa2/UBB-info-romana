from domain.student import Student
from exceptii.eroare_repo import EroareRepo


class RepositoryStudentiFisier:
    def __init__(self, filename):
        self.__filename = filename
        self.__studenti = {}
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__filename, 'r') as fisier:
                linii = fisier.readlines()
                for linie in linii:
                    linie = linie.strip()
                    if linie != "":
                        parti = linie.split(",")
                        id_student = int(parti[0])
                        nume = parti[1]
                        grup = int(parti[2])
                        # NU mai citim sters=True/False
                        student = Student(id_student, nume, grup)
                        self.__studenti[id_student] = student
        except FileNotFoundError:
            # Daca fisierul nu exista, pornim cu el gol
            pass

    def __save_to_file(self):
        with open(self.__filename, 'w') as f:
            for id in self.__studenti:
                student = self.__studenti[id]
                # NU mai scriem is_sters()
                f.write(f"{student.get_id_student()},{student.get_nume()},{student.get_grup()}\n")

    def __len__(self):
        return len(self.__studenti)

    def adauga_student(self, student):
        id_student = student.get_id_student()
        if id_student in self.__studenti:
            raise EroareRepo("id student existent!")
        self.__studenti[id_student] = student
        self.__save_to_file()

    def sterge_student(self, id_student):
        if id_student not in self.__studenti:
            raise EroareRepo("id student inexistent!")
        del self.__studenti[id_student]
        self.__save_to_file()

    def actualizeaza_student(self, id_student, id_nou, nume_nou, grup_nou):
        if id_student not in self.__studenti:
            raise EroareRepo("id student inexistent!")

        student = self.__studenti[id_student]

        if id_student != id_nou:
            if id_nou in self.__studenti:
                raise EroareRepo("id student nou existent!")
            del self.__studenti[id_student]
            student.set_id(id_nou)
            self.__studenti[id_nou] = student

        student.set_nume(nume_nou)
        student.set_grup(grup_nou)
        self.__save_to_file()

    def get_all(self):
        return list(self.__studenti.values())

    def get_student_dupa_id(self, id_student):
        if id_student in self.__studenti:
            return self.__studenti[id_student]
        raise EroareRepo("id student inexistent!")