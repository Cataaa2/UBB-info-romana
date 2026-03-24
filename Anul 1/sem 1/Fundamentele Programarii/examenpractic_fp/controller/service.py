from repository.repo_sedinte import Repository


class Service:
    def __init__(self,repo: Repository,validator):
        self.__repo = repo
        self.__validator = validator
        self.filtru_data = ""

    def get_all_sedinte(self):
        """
        functie care returneaza toate sedintele actuale
        """
        return self.__repo.get_all_sedinte()

    def get_sedinte_ziua_urmatoare(self):
        """
        functie care returneaza o lista cu sedintele din urmatoarea zi
        """
        return self.__repo.get_sedinte_ziua_urmatoare()

    def add(self,sedinta_noua):
        """
        functie pentru adaugarea unei esdinte
        """
        self.__validator.valideaza_sedinta(sedinta_noua)
        self.__repo.add(sedinta_noua)

    def export(self, nume_fisier, sir_subiect):
        self.__repo.export(nume_fisier, sir_subiect)

    def get_filtru_data(self):
        return self.filtru_data

    def set_filtru_data(self,new):
        self.filtru_data = new

    def get_urm_3zile(self):
        if self.filtru_data != "":
            de_afisat = []
            sedinte = self.get_all_sedinte()
            parti_filtru = self.filtru_data.split(".")
            dd_f = int(parti_filtru[0])
            mm_f = int(parti_filtru[1])
            for s in sedinte:
                data_sedinta = s.get_data()
                parti_data = data_sedinta.split(".")
                zi_sedinta = int(parti_data[0])
                luna_sedinta = int(parti_data[1])
                if luna_sedinta == mm_f:
                    if zi_sedinta > dd_f and zi_sedinta < (dd_f+4):
                        de_afisat.append(s)
            return de_afisat
        else:
            return ""
