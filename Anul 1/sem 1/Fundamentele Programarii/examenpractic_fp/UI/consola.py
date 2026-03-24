from controller.service import Service
from domain.sedinta import Sedinta
from exceptii.eroare_repo import EroareRepo
from exceptii.eroare_validator import EroareValidator


class Consola:
    def __init__(self,service: Service):
        self.__service = service

    def print_menu(self):
        print("-----MENU-----")
        print("0.Exit")
        print("1.Adaugare sedinta")
        print("2.Setare data")
        print("3.Export sedinte in fisier")
        print("4.Show all")

    def get_sedinte_ziua_urmatoare(self):
        sedinte_ziua_urmatoare = self.__service.get_sedinte_ziua_urmatoare()
        print("-----Sedinte ziua urmatoare-----")
        for s in sedinte_ziua_urmatoare:
            print(s)

    def show_all(self):
        sedinte = self.__service.get_all_sedinte()
        for s in sedinte:
            print(s)

    def add(self):
        data = input("Data sedintei (dd.mm): ")
        ora = input("Ora (hh:mm): ")
        subiect = input("Subiectul: ")
        fel = input("Fel (normal/extraordinar): ")
        sedinta_noua = Sedinta(data, ora, subiect, fel)
        self.__service.add(sedinta_noua)

    def setare_data(self):
        filtru_data = input("introduceti data(dd.mm): ")
        self.__service.set_filtru_data(filtru_data)
        print("Filtru setat cu succes!")

    def afisare_filtrate(self):
        filtrate = self.__service.get_urm_3zile()
        if filtrate != "":
            print("Sedinte din urmatoarele 3 zile: ")
            for s in filtrate:
                print(s)
            print("")

    def export(self):
        nume_fisier = input("nume fisier: ")
        sir_subiect = input("sir subiect: ")
        self.__service.export(nume_fisier, sir_subiect)

    def run(self):
        while True:
            self.get_sedinte_ziua_urmatoare()
            self.afisare_filtrate()
            self.print_menu()
            opt = input("Alegeti optiunea: ")
            try:
                match opt:
                    case '0':
                        print("bye")
                        break

                    case '1':
                        self.add()

                    case '2':
                        self.setare_data()

                    case '3':
                        self.export()

                    case '4':
                        self.show_all()
            except EroareRepo as e:
                print(e)
            except EroareValidator as e:
                print(e)