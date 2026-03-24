class Carte:
    def __init__(self,pseudo_isbn,autor,titlu,pret_pe_zi):
        """
        functie care creeaza o carte cu:
        :param pseudo_isbn: string
        :param autor: string
        :param titlu: string
        :param pret_pe_zi: int
        """
        self.__pseudo_isbn = pseudo_isbn
        self.__autor = autor
        self.__titlu = titlu
        self.__pret_pe_zi = pret_pe_zi

    def get_pseudo_isbn(self):
        """
        getter pentru pseudo isbn
        :return: str pseudo_isbn
        """
        return self.__pseudo_isbn

    def get_autor(self):
        """
        getter pentru autor
        :return: str autor
        """
        return self.__autor

    def get_titlu(self):
        """
        getter pentru titlu
        :return: str titlu
        """
        return self.__titlu

    def get_pret_pe_zi(self):
        """
        getter pentru pretul pe zi
        :return: pret_pe_zi
        """
        return self.__pret_pe_zi

    def __str__(self):
        """
        functie pentru afisarea unei carti
        """
        return f"Pseudo_isbn: {self.__pseudo_isbn}, autor: {self.__autor}, titlu: {self.__titlu}, pret_pe_zi: {self.__pret_pe_zi}"
