class ProblemaLaborator:

    def __init__(self, nrlab, nrproblema, descriere, deadline):
        """
        functie care creeaza o problema de laborator cu:
        :param nrlab: int
        :param nrproblema: int
        :param descriere: str
        :param deadline: int
        """
        self.__nrlab = nrlab
        self.__nrproblema = nrproblema
        self.__descriere = descriere
        self.__deadline = deadline

    def get_nrlab(self):
        return self.__nrlab

    def get_nrproblema(self):
        return self.__nrproblema

    def get_descriere(self):
        return self.__descriere

    def get_deadline(self):
        return self.__deadline

    def set_nrlab(self, nrlab_nou):
        self.__nrlab = nrlab_nou

    def set_nrproblema(self, nrproblema_noua):
        self.__nrproblema = nrproblema_noua

    def set_descriere(self, descriere_noua):
        self.__descriere = descriere_noua

    def set_deadline(self, deadline_nou):
        self.__deadline = deadline_nou

    def __str__(self):
        return f"{self.__nrlab}_{self.__nrproblema}: '{self.__descriere}' , deadline: {self.__deadline} zile"