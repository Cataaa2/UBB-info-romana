import unittest

from UI.consola import Console
from controller.service_note import ServiceNote
from controller.service_probleme_laboratoare import ServiceProblemeLaboratoare
from controller.service_studenti import ServiceStudenti
from repo_files.repo_note_file import RepositoryNoteFisier
from repo_files.repo_probleme_laboratoare_file import RepositoryProblemeLaboratoareFisier
from repo_files.repo_studenti_file import RepositoryStudentiFisier
from repository.repo_note import RepositoryNote
from repository.repo_probleme_laboratoare import RepositoryProblemeLaboratoare
from repository.repo_studenti import RepositoryStudenti
from testare.teste import Teste
from validare.validator_nota import ValidatorNota
from validare.validator_problema_laborator import ValidatorProblemaLaborator
from validare.validator_student import ValidatorStudent

fisier_studenti = r"C:\Users\Catalin\PycharmProjects\PythonProject\studenti.txt"
repo_studenti = RepositoryStudentiFisier(fisier_studenti)
fisier_probleme_laborator = r"C:\Users\Catalin\PycharmProjects\PythonProject\probleme_laborator.txt"
repo_probleme_laboratoare = RepositoryProblemeLaboratoareFisier(fisier_probleme_laborator)
fisier_note = r"C:\Users\Catalin\PycharmProjects\PythonProject\note.txt"
repo_note = RepositoryNoteFisier(fisier_note)

validator_student = ValidatorStudent()
validator_problema_laborator = ValidatorProblemaLaborator()
validator_nota = ValidatorNota()

service_studenti = ServiceStudenti(repo_studenti,validator_student)
service_probleme_laboratoare = ServiceProblemeLaboratoare(repo_probleme_laboratoare,validator_problema_laborator)
service_note = ServiceNote(repo_studenti,repo_probleme_laboratoare,repo_note,validator_nota)

teste = Teste()

ui = Console(service_studenti,service_probleme_laboratoare,service_note)

# teste.ruleaza_toate_testele()

ui.run()
