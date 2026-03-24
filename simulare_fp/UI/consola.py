from exceptii.eroare_repo import EroareRepo
from exceptii.eroare_ui import EroareUI


class Consola:
    def __init__(self,service_carti):
        self.__service_carti = service_carti
        #dictionar de comenzi:
        self.__comenzi = {
            "cauta_autor":self.__ui_cauta_dupa_autor,
            "imprumuta_carte":self.__ui_imprumuta_carte,
            # "help":self.__ui_help
        }

    def __ui_cauta_dupa_autor(self,parametri_comanda):
        """
        Functie care afiseaza cartile cu autorul dat, daca exista, sau "Nu exista carti scrise de acest autor!!" altfel
        raise EroareUI daca nu se introduce cel putin un parametru
        """
        if len(parametri_comanda) < 1:
            raise EroareUI("numar invalid de parametri!! trebuie minim 1 (nume)")
        nume = ""
        # formarea numelui introdus de uitilizator
        for cuvant in parametri_comanda:
            nume += cuvant + " "
        nume = nume.strip()
        carti_cautate = self.__service_carti.find_by_autor(nume)
        if not carti_cautate:
            # daca nu exista carti scrise de autorul cautat
            print("Nu exista carti scrise de acest autor!!")
        for pseudo_isbn in carti_cautate:
            carte = carti_cautate[pseudo_isbn]
            print(carte)

    def __ui_imprumuta_carte(self,parametri_comanda):
        """
        Functie care afiseaza cartea imprumutata si pretul total al inchirierii
        Raise EroareUI daca nu sunt introdusi 2 parametrii
        Raise ValueError daca numarul de zile <=0
        """
        if len(parametri_comanda) != 2:
            raise EroareUI("numar invalid de parametrii! trebuie 2 (pseudo_isbn, numar de zile)")
        pseudo_isbn = parametri_comanda[0]
        try:
            nr_de_zile = int(parametri_comanda[1])
            if nr_de_zile <= 0:
                raise ValueError
        except ValueError:
            print("numar invalid de zile pentru a imprumuta cartea!!")
            return
        imprumut = self.__service_carti.imprumuta_carte(pseudo_isbn,nr_de_zile)
        print(f"Ati imprumutat cartea: {imprumut[0]}")
        print(f"Pret total pentru {nr_de_zile} zile: {imprumut[1]}")

    # def __ui_help(self,parametri_comanda):
    #     print("-----COMENZI-----")
    #     print("'cauta_autor'")
    #     print("'imprumuta_carte'")

    def run(self):
        """
        Functie care porneste aplicatia
        "exit" pentru oprire
        """
        while True:
            # self.__ui_afisare_comenzi()
            text_comanda = input(">>>").strip()
            if text_comanda == "":
                continue
            if text_comanda == "exit":
                print("Goodbye!")
                break
            parti_comanda = text_comanda.split()
            nume_comanda = parti_comanda[0]
            parametri_comanda = parti_comanda[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda](parametri_comanda)
                except EroareUI as eroare_ui:
                    print(eroare_ui)
                except EroareRepo as eroare_repo:
                    print(eroare_repo)
            else:
                print("comanda invalida!!")