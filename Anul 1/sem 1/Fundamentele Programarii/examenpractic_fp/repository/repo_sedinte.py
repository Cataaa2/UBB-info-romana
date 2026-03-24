from domain.sedinta import Sedinta
import datetime

from exceptii.eroare_repo import EroareRepo


class Repository:
    def __init__(self,filename):
        self.__filename = filename
        self.__sedinte = []
        self.__load_from_file()

    def __load_from_file(self):
        """
        functie care incarca datele din fisier
        """
        with open(self.__filename,'r') as f:
            linii = f.readlines()
            for linie in linii:
                linie = linie.strip()
                if linie!= "":
                    parti = linie.split(",")
                    data = parti[0]
                    ora = parti[1]
                    subiect = parti[2]
                    fel = parti[3]
                    sedinta  = Sedinta(data,ora,subiect,fel)
                    self.__sedinte.append(sedinta)

    def __save_to_file(self):
        """
        functie care salveaza datele in fisier
        """
        with open(self.__filename,'w') as f:
            for s in self.__sedinte:
                f.write(f"{s.get_data()},{s.get_ora()},{s.get_subiect()},{s.get_fel()}\n")

    def get_all_sedinte(self):
        """
        functie care returneaza toate sedintele actuale
        """
        return self.__sedinte

    def get_sedinte_ziua_urmatoare(self):
        """
        functie care returneaza toate sedintele din urmatoarea zi
        """
        data_azi = datetime.date.today()
        luna_azi = data_azi.month
        zi_azi = data_azi.day
        sedinte_ziua_urmatoare = []
        for s in self.__sedinte:
            data_sedinta = s.get_data()
            parti_data = data_sedinta.split(".")
            zi_sedinta = int(parti_data[0])
            luna_sedinta = int(parti_data[1])
            if luna_azi == luna_sedinta:
                if zi_azi == (zi_sedinta-1):
                    sedinte_ziua_urmatoare.append(s)
        sedinte_sortate_dupa_ora = sorted(sedinte_ziua_urmatoare,key=lambda x: x.get_ora())
        return sedinte_sortate_dupa_ora

    def add(self,sedinta_noua):
        """
        functie pentru adaugarea unei sedinte
        """
        for s in self.__sedinte:
            if s.get_subiect() == sedinta_noua.get_subiect():
                if s.get_fel() == sedinta_noua.get_fel():
                    raise EroareRepo("nu pot exista 2 sedinte cu acelasi subiect si fel")
        self.__sedinte.append(sedinta_noua)
        self.__save_to_file()

    def export(self,nume_fisier,sir_subiect):
        """
        functie care creeaza fisierul cu numele 'nume_fisier' si scrie in el toate sedintele ce contin 'sir_subiect'
        in subiect, in ordine crescatoare dupa data si ora
        :param nume_fisier:
        :param sir_subiect:
        :return:
        """
        sedinte_bune = []
        for s in self.__sedinte:
            if sir_subiect in s.get_subiect():
                sedinte_bune.append(s)
        sedinte_sortate = sorted(sedinte_bune, key=lambda x: x.get_ora())
        sedinte_sortate = sorted(sedinte_sortate, key=lambda x: x.get_data_obj())
        with open(nume_fisier, 'w') as f:
            for s in sedinte_sortate:
                f.write(f"{s.get_data()},{s.get_ora()},{s.get_subiect()},{s.get_fel()}\n")





