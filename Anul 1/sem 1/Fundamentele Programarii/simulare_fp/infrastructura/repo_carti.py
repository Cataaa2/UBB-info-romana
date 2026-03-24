from domeniu.Carte import Carte
from exceptii.eroare_repo import EroareRepo


class RepositoryCarti:
    def __init__(self,filename):
        """
        Functie care creeaza un repository pentru carti
        :param filename: PATH catre fisierul de carti(CSV)
        """
        self.__filename = filename
        self.__carti = {}   # {cheie: pseudo_isbn, valoare: Carte}
        self.__load_from_file()

    def __load_from_file(self):
        """
        Functie care citeste cartile din fisier si le adauga in repository
        """
        with open(self.__filename,'r') as f:
            linii = f.readlines()
            for linie in linii:
                linie = linie.strip()
                if linie != "":
                    parti = linie.split(",")
                    pseudo_isbn = parti[0]
                    autor = parti[1]
                    titlu = parti[2]
                    pret_pe_zi = parti[3]
                    #creeam cartea din fisier si o adugam in repository:
                    carte = Carte(pseudo_isbn, autor, titlu,pret_pe_zi)
                    self.__carti[pseudo_isbn] = carte

    def find_by_autor(self,autor_cautat):
        """
        Functie care returneaza toate cartile scrise de autorul dat
        :param autor_cautat: str
        """
        carti_cautate = {}
        for pseudo_isbn in self.__carti:
            #verificam autorul fiecarei carti daca este cel cautat
            carte = self.__carti[pseudo_isbn]
            autor = carte.get_autor()
            if autor == autor_cautat:
                carti_cautate[pseudo_isbn] = carte
        return carti_cautate

    def imprumuta_carte(self,pseudo_isbn):
        """
        Functie care returneaza cartea cautata dupa pseudo_isbn
        :param pseudo_isbn: str
        """
        if pseudo_isbn not in self.__carti:
            #aruncam exceptie daca cartea cautata nu exista
            raise EroareRepo("Nu exista o carte cu acest pseudo_isbn")
        return self.__carti[pseudo_isbn]



