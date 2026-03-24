from exceptii.eroare_validator import EroareValidator


class ValidatorProblemaLaborator:

    def valideaza_problema_laborator(self,problema_laborator):
        """
        functie care valideaza o problema de laborator
        :param problema_laborator: problema_laborator cu  nrlab int, nrproblema int, descriere str, deadline int
        :return: -,daca problema de laborator este valida
                    eroare "nr laborator invalid!\n" daca nr laborator <=0
                    eroare "nr problema invalid!\n" daca nr probelma <=0
                    eroare "descriere invalida!\n" daca descrierea este goala
                    eroare "deadline invalid!\n" daca deadline <=0
        """
        erori = ""
        if problema_laborator.get_nrlab() <= 0:
            erori += "nr laborator invalid!\n"
        if problema_laborator.get_nrproblema() <= 0:
            erori += "nr problema invalid!\n"
        if problema_laborator.get_descriere() == "":
            erori += "descriere invalida!\n"
        if problema_laborator.get_deadline() <= 0:
            erori += "deadline invalid!\n"
        if len(erori) > 0:
            raise EroareValidator(erori)