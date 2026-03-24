from domain.produs import Produs
from exceptii.eroare_repo import EroareRepo
import random


class RepositoryProduse:
    def __init__(self,filename):
        self.__filename = filename
        self.__produse = []
        self.__load_from_file()

    def __load_from_file(self):
        with open(self.__filename,'r') as f:
            linii = f.readlines()
            for linie in linii:
                linie = linie.strip()
                if linie != "":
                    parti = linie.split(",")
                    id = int(parti[0])
                    denumire = parti[1]
                    pret = float(parti[2])
                    produs = Produs(id,denumire,pret)
                    self.__produse.append(produs)

    def __save_to_file(self):
        with open(self.__filename, 'w') as f:
            for p in self.__produse:
                f.write(f"{p.get_id()},{p.get_denumire()},{p.get_pret()}\n")

    def get_all_produse(self):
        return self.__produse

    def adauga_produs(self,id,denumire,pret):
        produs_nou = Produs(id,denumire,pret)
        for p in self.__produse:
            if p.get_id() == id:
                raise EroareRepo("id existent")
        self.__produse.append(produs_nou)
        self.__save_to_file()

    def sterge_produse_dupa_cifra(self,cifra):
        lista_noua = []
        for p in self.__produse:
            id_str = str(p.get_id())
            if cifra not in id_str:
                lista_noua.append(p)
        sterse = len(self.__produse) - len(lista_noua)
        self.__produse = lista_noua
        self.__save_to_file()
        return sterse

    def set_produse(self,lista_noua):
        self.__produse = lista_noua
        self.__save_to_file()

    def modificare_pret(self,id,pret_nou):
        for p in self.__produse:
            if id == p.get_id():
                p.set_pret(pret_nou)
                self.__save_to_file()
                return
        raise EroareRepo("id inexistent")

    def importa(self,filename):
        adaugate = 0
        if ".txt" not in filename:
            filename += ".txt"
        with open(filename, 'r') as f:
            linii = f.readlines()
            for linie in linii:
                linie = linie.strip()
                if linie != "":
                    parti = linie.split(",")
                    id = int(parti[0])
                    denumire = parti[1]
                    existent = False
                    for p in self.__produse:
                        if p.get_id() == id:
                            existent = True
                    if not existent:
                        pret_random = random.randint(1, 125)
                        produs_nou = Produs(id,denumire,pret_random)
                        self.__produse.append(produs_nou)
                        adaugate += 1
        self.__save_to_file()
        return adaugate