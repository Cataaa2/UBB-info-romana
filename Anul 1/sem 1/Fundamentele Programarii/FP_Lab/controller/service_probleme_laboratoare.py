from domain.problema_laborator import ProblemaLaborator
import random

from exceptii.eroare_repo import EroareRepo
from exceptii.eroare_ui import EroareUI


class ServiceProblemeLaboratoare:

    def __init__(self,repo_probleme_laboratoare,validator_problema_laborator):
        self.__repo_probleme_laboratoare = repo_probleme_laboratoare
        self.__validator_problema_laborator = validator_problema_laborator

    def adauga_problema_laborator(self,nrlab,nrproblema,descriere,deadline):
        problema_laborator = ProblemaLaborator(nrlab,nrproblema,descriere,deadline)
        self.__validator_problema_laborator.valideaza_problema_laborator(problema_laborator)
        self.__repo_probleme_laboratoare.adauga_problema_laborator(problema_laborator)

    def sterge_problema_laborator(self,nrlab,nrproblema):
        self.__repo_probleme_laboratoare.sterge_problema_laborator(nrlab,nrproblema)

    def actualizeaza_prob_lab(self,nrlab_vechi,nrprob_vechi,nrlab_nou,nrprob_nou,descriere_noua,deadline_nou):
        problema = ProblemaLaborator(nrlab_nou,nrprob_nou,descriere_noua,deadline_nou)
        self.__validator_problema_laborator.valideaza_problema_laborator(problema)
        self.__repo_probleme_laboratoare.actualizeaza_prob_lab(nrlab_vechi,nrprob_vechi,nrlab_nou,nrprob_nou,descriere_noua,deadline_nou)

    def get_repo(self):
        return self.__repo_probleme_laboratoare

    def get_by_nrlab_nrprob(self,nrlab,nrprob):
        return self.__repo_probleme_laboratoare.get_by_nrlab_nrprob(nrlab,nrprob)

    def descriere_random(self, lungime=None):
        """
        Genereaza o descriere random, recursiv
        """
        litere = "abcdefghijklmnopqrstuvwxyz"
        if lungime is None:
            lungime = random.randint(2, 10)
        if lungime == 0:
            return ""
        return random.choice(litere) + self.descriere_random(lungime - 1)

    def generare_problema_random(self,n):
        generate = 0
        while generate < n:
            nrlab = random.randint(1, 100)
            nrprob = random.randint(1, 100)
            desc = self.descriere_random()
            deadline = random.randint(1, 30)
            problema = ProblemaLaborator(nrlab,nrprob,desc,deadline)
            try:
                self.__repo_probleme_laboratoare.adauga_problema_laborator(problema)
                generate += 1
            except EroareRepo:
                continue