from exceptii.eroare_repo import EroareRepo
from exceptii.eroare_ui import EroareUI
from exceptii.eroare_validator import EroareValidator

class Console:

    def __init__(self,service_studenti,service_probleme_laboratoare,service_note):
        self.__service_studenti = service_studenti
        self.__service_probleme_laboratoare = service_probleme_laboratoare
        self.__service_note = service_note
        self.__comenzi ={
            "adauga_student": self.__ui_adauga_student,
            "afisare_studenti": self.__ui_afiseaza_toti_studentii,
            "help": self.__ui_help,
            "adauga_problema":self.__ui_adauga_prob_lab,
            "afisare_probleme":self.__ui_afiseaza_probleme,
            "sterge_student":self.__ui_sterge_student,
            "sterge_problema":self.__ui_sterge_problema_laborator,
            "actualizeaza_student":self.__ui_actualizeaza_student,
            "actualizeaza_problema":self.__ui__actualizeaza_problema,
            "asignare_lab":self.__ui_asignare_laborator,
            "notare_lab":self.__ui_notare_laborator,
            "afisare_note":self.__ui_afisare_note,
            "cauta_student":self.__ui_cauta_student,
            "cauta_problema":self.__ui_cauta_problema,
            "student_random":self.__ui_student_random,
            "problema_random":self.__ui_problema_random,
            "asignare_random":self.__ui_asignare_random,
            "medii_sub_5":self.__ui_medii_sub_5,
            "studenti_problema":self.__ui_studenti_problema,
            "cea_mai_mare_medie":self.__ui_cea_mai_mare_medie,
        }

    def __ui_afiseaza_comenzi(self):
        print("----------------COMENZI----------------")
        print("'adauga_student' adauga un student cu ID, Nume, Grup.")
        print("'actualizeaza_student' actualizeaza un student ales")
        print("'afisare_studenti' afiseaza o lista cu toti studentii cu: id, numele si grupa lor.")
        print("'adauga_problema' adauga o problema de laborator cu: nr. lab, nr. problema, descriere, deadline(un nr de zile).")
        print("'actualizeaza_problema' actualizeaza o problema aleasa")
        print("'afisare_probleme' afiseaza lista cu toate problemele de laborator ,descrierea si deadline-ul lor.")
        print("'sterge_student' ID")
        print("'sterge_problema'(nr lab,nr problema)")
        print("'asignare_lab' id, nrlab, nrprob")
        print("'notare_lab' id, nrlab, nrprob")
        print("'cauta_student' id")
        print("'cauta_problema' nrlab, nrprob")
        print("'afisare_note'")
        print("'medii_sub_5' lista studentilor cu media notelor sub 5")
        print("'studenti_problema' nrlab, nrprob, criteriu (nume/nota)")
        print("'cea_mai_mare_medie'")

    def __ui_afisare_note(self,parametri_comanda):
        if len(parametri_comanda) != 0:
            raise EroareUI("numar invalid de parametri!! trebuie 0")
        note = self.__service_note.get_all()
        if not note:
            print("nu sunt note")
            return
        for id in note:
            student = self.__service_studenti.get_student_dupa_id(id)
            print("------------")
            print(f"Studentul: {student}")
            print("Probleme asignate:")
            for (nrlab, nrprob), nota in note[id].items():
                problema = self.__service_probleme_laboratoare.get_by_nrlab_nrprob(nrlab,nrprob)
                nota_afisata = nota if nota is not None else "fara nota"
                print(f"Problema {problema}, nota: {nota_afisata}")

    def __ui_cea_mai_mare_medie(self,parametri_comanda):
        if len(parametri_comanda) != 0:
            raise EroareUI("numar invalid de parametri!! trebuie 0")
        ids = self.__service_note.cea_mai_mare_medie()
        if not ids:
            print("niciun student cu o laboratoare notate")
        for id, medie in ids.items():
            student = self.__service_studenti.get_student_dupa_id(id)
            nume = student.get_nume()
            print(f"{nume}: media {medie}")

    def __ui_asignare_random(self,parametri_comanda):
        if len(parametri_comanda) != 1:
            raise EroareUI("numar invalid de parametri!! trebuie 1")
        try:
            val = int(parametri_comanda[0])
            if val < 0:
                raise ValueError
        except ValueError:
            raise EroareUI("introduceti o valoare naturala")
        self.__service_note.asignare_random(val)

    def __ui_problema_random(self,parametri_comanda):
        if len(parametri_comanda) != 1:
            raise EroareUI("numar invalid de parametri!! trebuie 1")
        try:
            val = int(parametri_comanda[0])
            if val < 0:
                raise ValueError
        except ValueError:
            raise EroareUI("introduceti o valoare naturala")
        self.__service_probleme_laboratoare.generare_problema_random(val)
        print(f"{val} probleme aleatorii generate cu succes")

    def __ui_student_random(self,parametri_comanda):
        if len(parametri_comanda) != 1:
            raise EroareUI("numar invalid de parametri!! trebuie 1")
        try:
            val = int(parametri_comanda[0])
            if val < 0:
                raise ValueError
        except ValueError:
            raise EroareUI("introduceti o valoare naturala")
        self.__service_studenti.genereaza_studenti_random(val)
        print(f"{val} studenti aleatorii generati cu succes")

    def __ui_adauga_student(self,parametri_comanda):
        if len(parametri_comanda) < 3:
            raise EroareUI("numar invalid de parametri!! trebuie 3")
        try:
            id_student = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid! introduceti o valoare intreaga")

        if len(parametri_comanda)>3:
            nume = ""
            for i in range(1,len(parametri_comanda)-1):
                nume += parametri_comanda[i] + " "
        else:
            nume = parametri_comanda[1]
        try:
            grup = int(parametri_comanda[-1])
        except ValueError:
            raise EroareUI("Grupul trebuie sa fie un numar intreg >= 0")
        self.__service_studenti.adauga_student(id_student, nume, grup)
        print("Student adaugat cu succes!")

    def __ui_afiseaza_toti_studentii(self,parametri_comanda):
        if len(parametri_comanda) != 0:
            raise EroareUI("numar invalid de parametri!! trebuie 0")
        repo_studenti = self.__service_studenti.get_repo()
        if len(repo_studenti) == 0:
            raise EroareUI("nu exista studenti")
        for student in repo_studenti.get_all():
            print(student)

    def __ui_sterge_student(self,parametri_comanda):
        if len(parametri_comanda) != 1:
            raise EroareUI("numar invalid de parametri!! trebuie 1(id)")
        try:
            id_student = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid! introduceti o valoare intreaga")
        self.__service_studenti.sterge_student(id_student)
        self.__service_note.sterge_student_in_note(id_student)
        print(f"Studentul cu ID: {id_student} a fost sters cu succes!")

    def __ui_actualizeaza_student(self,parametri_comanda):
        if len(parametri_comanda) != 1:
            raise EroareUI("numar invalid de parametri!trebuie 1 (id student care trebuie actualizat)")
        try:
            id_student = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid! introduceti o valoare intreaga")
        try:
            id_nou = int(input("ID nou:"))
        except ValueError:
            raise EroareUI("id numeric invalid! introduceti o valoare intreaga")
        nume_nou = input("nume nou: ")
        try:
            grup_nou = int(input("grup nou: "))
        except ValueError:
            raise EroareUI("Grupul trebuie sa fie un numar intreg >= 0")
        self.__service_studenti.actualizeaza_student(id_student,id_nou,nume_nou,grup_nou)
        self.__service_note.actualizeaza_id_student_in_note(id_student, id_nou)
        print("Student actualizat cu succes!")

    def __ui_adauga_prob_lab(self,parametri_comanda):
        if len(parametri_comanda) <4 :
            raise EroareUI("numar invalid de parametri!! trebuie 4(nrlab, nrprob, descriere, deadline)")
        try:
            nrlab = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("nr laborator trebuie sa fie intreg si >0")
        try:
            nrproblema = int(parametri_comanda[1])
        except ValueError:
            raise EroareUI("nr problema trebuie sa fie intreg si >0")
        cuvinte = parametri_comanda[2:len(parametri_comanda)-1]
        descriere = ""
        for cuvant in cuvinte:
            descriere += cuvant + " "
        descriere = descriere.strip()
        try:
            deadline = int(parametri_comanda[len(parametri_comanda)-1])
        except ValueError:
            raise EroareUI("deadline-ul trebuie sa fie intreg si >0")
        self.__service_probleme_laboratoare.adauga_problema_laborator(nrlab,nrproblema,descriere,deadline)
        print("Problema laborator adaugata cu succes!")

    def __ui_afiseaza_probleme(self,parametri_comanda):
        if len(parametri_comanda) != 0:
            raise EroareUI("numar invalid de parametri!! trebuie 0")
        repo_probleme_laboratoare = self.__service_probleme_laboratoare.get_repo()
        if len(repo_probleme_laboratoare) == 0:
            raise EroareUI("nu exista probleme de laborator")
        for problema_laborator in repo_probleme_laboratoare.get_all():
            print(problema_laborator)

    def __ui_sterge_problema_laborator(self,parametri_comanda):
        if len(parametri_comanda) != 2:
            raise EroareUI("numar invalid de parametri!! trebuie 2 (nr laborator, nr problema)")
        try:
            nrlab = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("nr laborator trebuie sa fie intreg si >0")
        try:
            nrproblema = int(parametri_comanda[1])
        except ValueError:
            raise EroareUI("nr problema trebuie sa fie intreg si >0")
        self.__service_probleme_laboratoare.sterge_problema_laborator(nrlab,nrproblema)
        self.__service_note.sterge_problema_in_note(nrlab,nrproblema)
        print(f"Problema laborator: {nrlab}_{nrproblema} a fost stearsa cu succes!")

    def __ui__actualizeaza_problema(self,parametri_comanda):
        if len(parametri_comanda) != 2:
            raise EroareUI("numar invalid de parametri!! trebuie 2(nr laborator, nr problema)")
        try:
            nrlab_vechi = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("nr laborator trebuie sa fie intreg si >0")
        try:
            nrprob_vechi = int(parametri_comanda[1])
        except ValueError:
            raise EroareUI("nr problema trebuie sa fie intreg si >0")
        try:
            nrlab_nou = int(input("nr lab nou:"))
        except ValueError:
            raise EroareUI("nr laborator trebuie sa fie intreg si >0")
        try:
            nrprob_nou = int(input("nr problema nou:"))
        except ValueError:
            raise EroareUI("nr problema trebuie sa fie intreg si >0")
        descriere = input("descriere:")
        try:
            deadline_nou = int(input("deadline nou:"))
        except ValueError:
            raise EroareUI("deadline-ul trebuie sa fie intreg si >0")
        self.__service_probleme_laboratoare.actualizeaza_prob_lab(nrlab_vechi,nrprob_vechi,nrlab_nou,nrprob_nou,descriere,deadline_nou)
        self.__service_note.actualizeaza_lab_in_note(nrlab_vechi,nrprob_vechi,nrlab_nou,nrprob_nou)
        print("problema actualizata cu succes!")

    def __ui_asignare_laborator(self,parametri_comanda):
        if len(parametri_comanda) != 3:
            raise EroareUI("numar invalid de parametri!! trebuie 3(id, nrlab, nrprob)")
        try:
            id_student = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid! introduceti o valoare intreaga")
        try:
            nrlab = int(parametri_comanda[1])
        except ValueError:
            raise EroareUI("nr laborator trebuie sa fie intreg si >0")
        try:
            nrproblema = int(parametri_comanda[2])
        except ValueError:
            raise EroareUI("nr problema trebuie sa fie intreg si >0")
        self.__service_note.asignare_laborator(id_student,nrlab,nrproblema)
        print(f"Problema {nrlab}_{nrproblema} asignata studentului cu ID: {id_student} cu succes!!")

    def __ui_notare_laborator(self,parametri_comanda):
        if len(parametri_comanda) != 3:
            raise EroareUI("numar invalid de parametri!! trebuie 3(id, nrlab, nrprob")
        try:
            id_student = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("id numeric invalid! introduceti o valoare intreaga")
        try:
            nrlab = int(parametri_comanda[1])
        except ValueError:
            raise EroareUI("nr laborator trebuie sa fie intreg si >0")
        try:
            nrproblema = int(parametri_comanda[2])
        except ValueError:
            raise EroareUI("nr problema trebuie sa fie intreg si >0")
        try:
            nota = float(input("nota: "))
        except ValueError:
            raise EroareUI("nota invalida! introduceti o valoare intre 1 si 10")
        self.__service_note.notare_laborator(id_student,nrlab,nrproblema,nota)
        print("Laborator notat cu succes!")

    def __ui_cauta_student(self, parametri_comanda):
        if len(parametri_comanda) != 1:
            raise EroareUI("numar invalid de parametri!! trebuie 1(id student)")
        try:
            id_student = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("ID-ul trebuie sa fie un numar intreg")
        note_student = self.__service_note.get_note_student(id_student)
        repo_studenti = self.__service_studenti.get_repo()
        student = repo_studenti.get_student_dupa_id(id_student)
        if not note_student:
            print(f"{student}. Niciun laborator asignat")
            return
        print(f"Date student: {student}. Laboratoare asignate:")
        for (nrlab, nrprob), nota in note_student.items():
            nota_afisata = nota if nota is not None else "fara nota"
            print(f"Laborator {nrlab}, Problema {nrprob}: {nota_afisata}")

    def __ui_cauta_problema(self,parametri_comanda):
        if len(parametri_comanda) != 2:
            raise EroareRepo("numar invalid de parametri!! trebuie 2(nrlab, nrprob)")
        try:
            nrlab = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("nr laborator trebuie sa fie intreg si >0")
        try:
            nrprob = int(parametri_comanda[1])
        except ValueError:
            raise EroareUI("nr problema trebuie sa fie intreg si >0")
        note = self.__service_note.get_all()
        cheie = (nrlab, nrprob)
        repo_probleme_laboratoare = self.__service_probleme_laboratoare.get_repo()
        problema = repo_probleme_laboratoare.get_by_nrlab_nrprob(nrlab,nrprob)
        print(f"Date problema: {problema}")
        # note = {id_student: {(nrlab,nrprob): nota}}
        gasit = False
        for id,laburi in note.items():
            laburi_student = self.__service_note.get_note_student(id)
            if cheie in laburi_student:
                if not gasit:
                    print("Problema este asignata studentilor cu id:")
                    gasit = True
                print(f"{id}")
        if not gasit:
            print("Problema nu este asignata niciunui student!")

    def __ui_medii_sub_5(self,parametri_comanda):
        if len(parametri_comanda) != 0:
            raise EroareUI("numar invalid de parametri!! trebuie 0")
        ids = self.__service_note.medii_sub5()
        if not ids:
            print("niciun student cu media sub 5")
        for id, medie in ids.items():
            student = self.__service_studenti.get_student_dupa_id(id)
            nume = student.get_nume()
            print(f"{nume}: media {medie}")

    def __ui_studenti_problema(self, parametri_comanda):
        if len(parametri_comanda) != 3:
            raise EroareUI("numar invalid de parametri!! trebuie 3 (nrlab, nrprob, criteriu[nume/nota])")
        try:
            nrlab = int(parametri_comanda[0])
        except ValueError:
            raise EroareUI("nr laborator trebuie sa fie intreg si >0")
        try:
            nrprob = int(parametri_comanda[1])
        except ValueError:
            raise EroareUI("nr problema trebuie sa fie intreg si >0")
        criteriu = parametri_comanda[2]
        if criteriu not in ["nume", "nota"]:
            raise EroareUI("criteriul trebuie sa fie 'nume' sau 'nota'!")

        lista_studenti = self.__service_note.studenti_cu_problema_data(nrlab, nrprob, criteriu)
        problema = self.__service_probleme_laboratoare.get_repo().get_by_nrlab_nrprob(nrlab, nrprob)
        if not lista_studenti:
            print("niciun student cu aceasta problema notata")
            return
        print(f"Lista de studenți și notele lor la problema **{problema}** ordonată după {criteriu}:")
        for id, nota in lista_studenti.items():
            student = self.__service_studenti.get_student_dupa_id(id)
            print(f"{student}, nota: {nota}")

    def __ui_help(self,parametri_comanda):
        if len(parametri_comanda) != 0:
            raise EroareUI("numar invalid de parametri!! trebuie 0")
        self.__ui_afiseaza_comenzi()

    def run(self):
        while True:
            text_comanda = input(">>>").strip().lower()
            if text_comanda == "":
                continue
            if text_comanda == "exit":
                print("bye!!")
                return
            parti_comanda = text_comanda.split()
            nume_comanda = parti_comanda[0]
            parametri_comanda = parti_comanda[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda](parametri_comanda)
                except EroareUI as eroare_ui:
                    print(eroare_ui)
                except EroareRepo as eroare_repo:
                    print(eroare_repo)
                except EroareValidator as eroare_validator:
                    print(eroare_validator)
            else:
                print("Comanda invalida! Scrieti 'help' pentru comenzi valide")
