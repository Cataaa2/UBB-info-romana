class ServiceCarti:
    def __init__(self,repo_carti):
        """
        Functie care creeaza service-ul pentru carti
        :param repo_carti: RepositoryCarti
        """
        self.__repo_carti = repo_carti

    def find_by_autor(self,autor):
        """
        Functie care returneaza toate cartile scrise de autorul dat
        :param autor: str
        """
        return self.__repo_carti.find_by_autor(autor)

    def imprumuta_carte(self,pseudo_isbn,numar_de_zile):
        """
        Functie care returneaza cartea cautata dupa pseudo_isbn si pretul total
        :param pseudo_isbn: str
        :param numar_de_zile: int
        :return lista
        """
        imprumut = []
        carte = self.__repo_carti.imprumuta_carte(pseudo_isbn)
        pret_total = int(carte.get_pret_pe_zi()) * int(numar_de_zile)
        imprumut.append(carte)
        imprumut.append(pret_total)
        return imprumut
