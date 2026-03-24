from domain.problema_laborator import ProblemaLaborator
from exceptii.eroare_repo import EroareRepo


class RepositoryProblemeLaboratoareFisier:

    def __init__(self, filename):
        self.__filename = filename
        self.__probleme_laboratoare = {}
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__filename, 'r') as f:
                linii = f.readlines()
                for linie in linii:
                    linie = linie.strip()
                    if linie != "":
                        parti = linie.split(",")
                        nrlab = int(parti[0])
                        nrprob = int(parti[1])
                        descriere = parti[2]
                        deadline = int(parti[3])
                        problema = ProblemaLaborator(nrlab, nrprob, descriere, deadline)
                        cheie = (nrlab, nrprob)
                        self.__probleme_laboratoare[cheie] = problema
        except FileNotFoundError:
            pass

    def __save_to_file(self):
        with open(self.__filename, 'w') as f:
            for cheie in self.__probleme_laboratoare:
                problema = self.__probleme_laboratoare[cheie]
                f.write(
                    f"{problema.get_nrlab()},{problema.get_nrproblema()},{problema.get_descriere()},{problema.get_deadline()}\n")

    def __len__(self):
        return len(self.__probleme_laboratoare)

    def adauga_problema_laborator(self, problema_laborator):
        nrlab = problema_laborator.get_nrlab()
        nrprob = problema_laborator.get_nrproblema()
        cheie = (nrlab, nrprob)
        if cheie in self.__probleme_laboratoare:
            raise EroareRepo("laboratorul si problema exista deja!")
        self.__probleme_laboratoare[cheie] = problema_laborator
        self.__save_to_file()

    def sterge_problema_laborator(self, nrlab, nrproblema):
        cheie = (nrlab, nrproblema)
        if cheie not in self.__probleme_laboratoare:
            raise EroareRepo("nr laborator,problema inexistente!")
        del self.__probleme_laboratoare[cheie]
        self.__save_to_file()

    def actualizeaza_prob_lab(self, nrlab_vechi, nrprob_vechi, nrlab_nou, nrprob_nou, descriere_noua, deadline_nou):
        cheie_veche = (nrlab_vechi, nrprob_vechi)
        if cheie_veche not in self.__probleme_laboratoare:
            raise EroareRepo("nr laborator,problema inexistente!")

        cheie_noua = (nrlab_nou, nrprob_nou)
        problema = self.__probleme_laboratoare[cheie_veche]

        if cheie_veche != cheie_noua:
            if cheie_noua in self.__probleme_laboratoare:
                raise EroareRepo("laboratorul si problema exista deja!")
            del self.__probleme_laboratoare[cheie_veche]
            problema.set_nrlab(nrlab_nou)
            problema.set_nrproblema(nrprob_nou)
            self.__probleme_laboratoare[cheie_noua] = problema

        problema.set_descriere(descriere_noua)
        problema.set_deadline(deadline_nou)
        self.__save_to_file()

    def get_by_nrlab_nrprob(self, nrlab, nrprob):
        cheie = (nrlab, nrprob)
        if cheie in self.__probleme_laboratoare:
            return self.__probleme_laboratoare[cheie]
        raise EroareRepo("nr laborator,problema inexistente!")

    def get_all(self):
        return list(self.__probleme_laboratoare.values())