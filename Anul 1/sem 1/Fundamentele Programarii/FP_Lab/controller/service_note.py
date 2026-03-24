import random

from utils.sortari import sortare_generica


class ServiceNote:
    def __init__(self,repo_studenti,repo_probleme_laboratoare,repo_note,validator_nota):
        self.__repo_studenti = repo_studenti
        self.__repo_probleme_laboratoare = repo_probleme_laboratoare
        self.__repo_note = repo_note
        self.__validator_nota = validator_nota

    def asignare_laborator(self, id_student, nrlab, nrproblema):
        self.__repo_studenti.get_student_dupa_id(id_student)
        self.__repo_probleme_laboratoare.get_by_nrlab_nrprob(nrlab, nrproblema)
        self.__repo_note.asignare_laborator(id_student, nrlab, nrproblema)

    def notare_laborator(self, id_student, nrlab, nrproblema, nota):
        self.__repo_studenti.get_student_dupa_id(id_student)
        self.__repo_probleme_laboratoare.get_by_nrlab_nrprob(nrlab, nrproblema)
        self.__validator_nota.valideaza_nota(nota)
        self.__repo_note.notare_laborator(id_student, nrlab, nrproblema, nota)

    def get_note_student(self,id_student):
        return self.__repo_note.get_note_student(id_student)

    def get_all(self):
        return self.__repo_note.get_all()

    def actualizeaza_id_student_in_note(self, id_vechi, id_nou):
        self.__repo_note.actualizeaza_id_student(id_vechi, id_nou)

    def actualizeaza_lab_in_note(self,lab_vechi,prob_vechie,lab_nou,prob_noua):
        self.__repo_note.actualizeaza_lab(lab_vechi,prob_vechie,lab_nou,prob_noua)

    def sterge_student_in_note(self, id_student):
        self.__repo_note.sterge_student(id_student)

    def sterge_problema_in_note(self, nrlab, nrproblema):
        self.__repo_note.sterge_problema(nrlab, nrproblema)

    def medii_sub5(self):
        return self.__repo_note.medii_sub5()

    def studenti_cu_problema_data(self,nrlab,nrprob,criteriu):
        note_studenti = self.__repo_note.studenti_cu_problema_data(nrlab, nrprob)
        return self.sortare_studenti(note_studenti,criteriu)

    def cea_mai_mare_medie(self):
        return self.__repo_note.cea_mai_mare_medie()

    def asignare_random(self, n):
        studenti = self.__repo_studenti.get_all()
        probleme = self.__repo_probleme_laboratoare.get_all()
        if not studenti or not probleme:
            return
        generate = 0
        while generate < n:
            stud = random.choice(studenti)
            prob = random.choice(probleme)
            id_stud = stud.get_id_student()
            nrlab = prob.get_nrlab()
            nrprob = prob.get_nrproblema()
            try:
                self.__repo_note.asignare_laborator(id_stud, nrlab, nrprob)
                generate += 1
            except:
                continue

    def __cheie_sortare_nume(self, element_lista):
        """ Returneaza (nume, nota) - sorteaza primar dupa nume """
        id_stud = element_lista[0]
        nota = element_lista[1]
        student = self.__repo_studenti.get_student_dupa_id(id_stud)
        return student.get_nume(), -nota

    def __cheie_sortare_nota(self, element_lista):
        """ Returneaza (nota, nume) - sorteaza primar dupa nota """
        id_stud = element_lista[0]
        nota = element_lista[1]
        student = self.__repo_studenti.get_student_dupa_id(id_stud)
        return nota, student.get_nume()

    def sortare_studenti(self, note_studenti, criteriu):
        lista_note = list(note_studenti.items())
        if criteriu == "nume":
            cheie = self.__cheie_sortare_nume
            reverse = False
        elif criteriu == "nota":
            cheie = self.__cheie_sortare_nota
            reverse = False
        else:
            cheie = self.__cheie_sortare_nume
            reverse=False
        sortare_generica(lista_note, key=cheie, reverse=reverse, algoritm='shell')
        lista_sortata = dict(lista_note)
        return lista_sortata