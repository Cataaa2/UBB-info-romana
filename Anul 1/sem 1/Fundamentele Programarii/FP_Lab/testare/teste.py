from controller.service_note import ServiceNote
from controller.service_probleme_laboratoare import ServiceProblemeLaboratoare
from controller.service_studenti import ServiceStudenti
from domain.problema_laborator import ProblemaLaborator
from domain.student import Student
from exceptii.eroare_repo import EroareRepo
from exceptii.eroare_validator import EroareValidator
from repository.repo_note import RepositoryNote
from repository.repo_probleme_laboratoare import RepositoryProblemeLaboratoare
from repository.repo_studenti import RepositoryStudenti
from validare.validator_nota import ValidatorNota
from validare.validator_problema_laborator import ValidatorProblemaLaborator
from validare.validator_student import ValidatorStudent
import unittest

class Teste(unittest.TestCase):

    def ruleaza_toate_testele(self):
        print("Rulare teste...")
        unittest.main()

    def setUp(self):
        self.validator_student = ValidatorStudent()
        self.repo_studenti = RepositoryStudenti()
        self.service_studenti = ServiceStudenti(self.repo_studenti,self.validator_student)

        self.validator_problema = ValidatorProblemaLaborator()
        self.repo_probleme = RepositoryProblemeLaboratoare()
        self.service_probleme = ServiceProblemeLaboratoare(self.repo_probleme,self.validator_problema)

        self.validator_nota = ValidatorNota()
        self.repo_note = RepositoryNote()
        self.service_note = ServiceNote(self.repo_studenti, self.repo_probleme, self.repo_note, self.validator_nota)

    def test_creeaza_student(self):
        id_student = 1
        nume = "Cata"
        grup = 1
        student = Student(id_student, nume, grup)
        self.assertTrue (id_student == student.get_id_student())
        self.assertTrue (nume == student.get_nume())
        self.assertTrue (grup == student.get_grup())

    def test_valideaza_student(self):
        id_student_invalid = -3
        nume_invalid = ""
        grup_invalid = -6
        student_invalid = Student(id_student_invalid, nume_invalid, grup_invalid)
        self.assertRaises(EroareValidator,self.validator_student.valideaza_student, student_invalid)

    def test_adauga_student(self):
        self.assertEqual(len(self.repo_studenti), 0)
        self.service_studenti.adauga_student(1, "ion", 3)
        self.assertEqual(len(self.repo_studenti), 1)
        with self.assertRaises(EroareRepo):
            self.service_studenti.adauga_student(1, "ion", 3)

    def test_sterge_student(self):
        self.service_studenti.adauga_student(1, "ion", 3)
        self.service_studenti.sterge_student(1)
        self.assertEqual(len(self.repo_studenti), 0)
        with self.assertRaises(EroareRepo):
            self.service_studenti.sterge_student(10)

    def test_actualizare_student(self):
        self.service_studenti.adauga_student(1, "ion", 3)
        self.service_studenti.adauga_student(2, "marian", 10)
        with self.assertRaises(EroareRepo):
            self.service_studenti.actualizeaza_student(1, 2, "Marian", 200)
        self.service_studenti.actualizeaza_student(1, 3, "Marian", 200)
        student_nou = self.repo_studenti.get_student_dupa_id(3)
        self.assertTrue(student_nou.get_nume() == "Marian")
        self.assertTrue(student_nou.get_grup() == 200)

    def test_creeaza_problema_laborator(self):
        nrlab= 3
        nrproblema= 2
        descriere = "catalog studenti"
        deadline = 7
        problema_laborator = ProblemaLaborator(nrlab, nrproblema, descriere, deadline)
        self.assertTrue (nrlab == problema_laborator.get_nrlab())
        self.assertTrue (nrproblema == problema_laborator.get_nrproblema())
        self.assertTrue (descriere == problema_laborator.get_descriere())
        self.assertTrue (deadline == problema_laborator.get_deadline())

    def test_valideaza_problema_laborator(self):
        nrlab_invalid = 0
        nrproblema_invalida = 0
        descriere_invalida = ""
        deadline_invalid = 0
        problema_laborator_invalida = ProblemaLaborator(nrlab_invalid, nrproblema_invalida, descriere_invalida,deadline_invalid)
        with self.assertRaises(EroareValidator):
            self.validator_problema.valideaza_problema_laborator(problema_laborator_invalida)

    def test_adauga_problema_laborator_repo(self):
        self.assertTrue (len(self.repo_probleme) == 0)
        problema_laborator = ProblemaLaborator(3,2,"catalog studenti",7)
        self.repo_probleme.adauga_problema_laborator(problema_laborator)
        self.assertTrue (len(self.repo_probleme) == 1)
        with self.assertRaises(EroareRepo):
            self.repo_probleme.adauga_problema_laborator(problema_laborator)

    def test_sterge_problema_laborator(self):
        self.assertTrue (len(self.repo_probleme) == 0)
        with self.assertRaises(EroareRepo):
            self.service_probleme.sterge_problema_laborator(5,10)
        self.service_probleme.adauga_problema_laborator(5,10,"tema",5)
        self.service_probleme.sterge_problema_laborator(5,10)
        self.assertTrue (len(self.repo_probleme) == 0)

    def test_actualizeaza_prob_lab(self):
        p1 = ProblemaLaborator(1,1,"catalog studenti",10)
        self.repo_probleme.adauga_problema_laborator(p1)
        p2 = ProblemaLaborator(2,2,"inchiriere firma",14)
        self.repo_probleme.adauga_problema_laborator(p2)
        with self.assertRaises(EroareRepo):
            self.service_probleme.actualizeaza_prob_lab(1, 1, 2, 2, "desc", 12)
        self.repo_probleme.actualizeaza_prob_lab(1,1,1,2,"tema",12)
        p1 = self.repo_probleme.get_by_nrlab_nrprob(1,2)
        self.assertTrue (p1.get_nrlab() == 1)
        self.assertTrue (p1.get_nrproblema() == 2)
        self.assertTrue (p1.get_descriere() == "tema")
        self.assertTrue (p1.get_deadline() == 12)
        self.assertTrue (len(self.repo_probleme) == 2)

    def adauga_student_problema(self,id,nrlab,nrprob):
        student = Student(id, "Ion", 101)
        problema = ProblemaLaborator(nrlab, nrprob, "tema 1", 7)
        self.repo_studenti.adauga_student(student)
        self.repo_probleme.adauga_problema_laborator(problema)

    def test_asignare_si_notare_laborator(self):
        self.adauga_student_problema(1,1,1)
        self.service_note.asignare_laborator(1, 1, 1)
        note_student = self.service_note.get_note_student(1)
        self.assertTrue ((1, 1) in note_student)
        self.assertTrue (note_student[(1, 1)] is None)
        self.service_note.notare_laborator(1, 1, 1, 9.5)
        note_student = self.service_note.get_note_student(1)
        self.assertTrue (note_student[(1, 1)] == 9.5)
        with self.assertRaises(EroareRepo):
            self.service_note.asignare_laborator(2, 1, 1)
        with self.assertRaises(EroareRepo):
            self.service_note.asignare_laborator(1, 2, 2)
        self.service_probleme.adauga_problema_laborator(2, 2, "tema 2", 7)
        with self.assertRaises(EroareRepo):
            self.service_note.notare_laborator(1,2,2,10)

    def setup_asignari(self):
        self.service_note.asignare_laborator(1, 1, 1)
        self.service_note.asignare_laborator(1, 2, 2)
        self.service_note.asignare_laborator(2, 2, 2)
        self.service_note.asignare_laborator(3, 3, 3)
        self.service_note.notare_laborator(1, 1, 1, 4)
        self.service_note.notare_laborator(1, 2, 2, 5)
        self.service_note.notare_laborator(2, 2, 2, 3.5)
        self.service_note.notare_laborator(3, 3, 3, 2.5)

    def test_raport_medii_sub_5(self):
        self.adauga_student_problema(1,1,1)
        self.adauga_student_problema(2, 2, 2)
        self.adauga_student_problema(3, 3, 3)
        ids = self.service_note.medii_sub5()
        self.assertTrue (ids == {})
        self.setup_asignari()
        ids = self.service_note.medii_sub5()
        self.assertTrue (ids[1] == 4.5)
        self.assertTrue (ids[2] == 3.5)
        self.assertTrue (ids[3] == 2.5)

    # def test_raport_studenti_problema(self):
    #     self.adauga_student_problema(1, 1, 1)
    #     self.adauga_student_problema(2, 2, 2)
    #     self.adauga_student_problema(3, 3, 3)
    #     lista_studenti = self.service_note.studenti_cu_problema_data(2,2)
    #     self.assertTrue (lista_studenti == {})
    #     self.setup_asignari()
    #     lista_studenti = self.service_note.studenti_cu_problema_data(2,2)
    #     self.assertTrue (lista_studenti[2] == 3.5)
    #     self.assertTrue (lista_studenti[1] == 5)
    #     lista_studenti = self.service_note.studenti_cu_problema_data(1, 1)
    #     self.assertTrue (lista_studenti[1] == 4)
    #     lista_studenti = self.service_note.studenti_cu_problema_data(3, 3)
    #     self.assertTrue (lista_studenti[3] == 2.5)

if __name__ == "__main__":
    unittest.main()