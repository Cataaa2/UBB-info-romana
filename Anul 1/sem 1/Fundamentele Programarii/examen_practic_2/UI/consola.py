from controller.service import Service
from exceptii.eroare_repo import EroareRepo
from exceptii.eroare_service import EroareService


class Consola:
    def __init__(self,service: Service):
        self.__service = service

    def print_menu(self):
        print("--------MENU--------")
        print("0.Exit")
        print("1.Adauga produs")
        print("2.Sterge dupa cifra id")
        print("3.Filtrare produse")
        print("4.Undo stergere")
        print("5.Show all")
        print("6.Modificare pret dupa id")
        print("7.Importa din fisier")
        print("\n")

    def show_all(self):
        produse = self.__service.get_all_produse()
        for p in produse:
            print(p)

    def citire_id(self):
        while True:
            try:
                id = int(input("ID: "))
                break
            except ValueError:
                print("id invalid introduceti o valoare numerica")
        return id

    def citire_denumire(self):
        while True:
            try:
                denumire = input("Denumire produs: ")
                if denumire.strip() != "":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("denumire invalida")
        return denumire.strip()

    def citire_pret(self):
        while True:
            try:
                pret = float(input("Pret produs:"))
                break
            except ValueError:
                print("introdu o valoare numerica ba")
        return pret

    def citire_produs(self):
        id = self.citire_id()
        denumire = self.citire_denumire()
        pret = self.citire_pret()
        return id,denumire,pret

    def adauga_produs(self):
        id,denumire,pret = self.citire_produs()
        self.__service.adauga_produs(id, denumire, pret)
        print("produs adaugat cu succes")

    def sterge_produse_dupa_cifra(self):
        cifra = input("cifra: ")
        nr_sterse = self.__service.sterge_produse_dupa_cifra(cifra)
        print(f"numar produse sterse: {nr_sterse}")

    def afisare_filtre_lista(self):
        f_denumire, f_pret = self.__service.get_filtre()
        produse_filtrate = self.__service.get_produse_filtrate()
        print(f"Filtre actuale: denumire={f_denumire}, pret={f_pret}")
        print("Lista produse filtrate:")
        for p in produse_filtrate:
            print(p)

    def set_filtre(self):
        f_denumire = input("filtru denumire: ")
        while True:
            try:
                f_pret = float(input("filtru pret: "))
                break
            except ValueError:
                print("introduceti o valoare numerica pentru filtrul de pret")
        self.__service.set_filtre(f_denumire,f_pret)
        print("Filtre noi setate cu succes\n")

    def undo(self):
        self.__service.undo()

    def modificare_pret(self):
        id = self.citire_id()
        pret_nou = self.citire_pret()
        self.__service.modificare_pret(id,pret_nou)
        print("Pret modificat cu succes\n")

    def importa(self):
        filename = input("Nume fisier din care se importa produse: ")
        adaugate = self.__service.importa(filename)
        print(f"Au fost adaugate: {adaugate} produse")

    def run(self):
        while True:
            self.print_menu()
            self.afisare_filtre_lista()
            comanda = input(">>>")
            try:
                match comanda:
                    case '0':
                        print("bye")
                        break

                    case '1':
                        self.adauga_produs()

                    case '2':
                        self.sterge_produse_dupa_cifra()

                    case '3':
                        self.set_filtre()

                    case '4':
                        self.undo()

                    case '5':
                        self.show_all()

                    case '6':
                        self.modificare_pret()

                    case '7':
                        self.importa()

                    case _:
                        print("optiune invalida")
            except EroareRepo as e:
                print(e)
            except EroareService as e:
                print(e)
