from Repository.repo_produse import RepositoryProduse
from copy import deepcopy

from exceptii.eroare_service import EroareService


class Service:
    def __init__(self,repo: RepositoryProduse):
        self.__repo = repo
        self.filtru_denumire = ""
        self.filtru_pret = -1
        self.__undolist = []

    def get_all_produse(self):
        return self.__repo.get_all_produse()

    def adauga_produs(self,id,denumire,pret):
        self.__repo.adauga_produs(id,denumire,pret)

    def sterge_produse_dupa_cifra(self,cifra):
        self.update_undolist()
        return self.__repo.sterge_produse_dupa_cifra(cifra)

    def set_filtre(self,filtru_denumire_nou,filtru_pret_nou):
        self.filtru_denumire = filtru_denumire_nou
        self.filtru_pret = filtru_pret_nou

    def get_filtre(self):
        return self.filtru_denumire,self.filtru_pret

    def get_produse_filtrate(self):
        f_denumire, f_pret = self.get_filtre()
        produse_filtrate = []
        produse = self.get_all_produse()
        for p in produse:
            if f_denumire in p.get_denumire() and p.get_pret() < f_pret:
                produse_filtrate.append(p)
        return produse_filtrate

    def update_undolist(self):
        produse = self.get_all_produse()
        self.__undolist.append(deepcopy(produse))

    def undo(self):
        if len(self.__undolist) == 0:
            raise EroareService("Nothing to undo!!\n")
        lista_noua = self.__undolist.pop()
        self.__repo.set_produse(lista_noua)

    def modificare_pret(self,id,pret_nou):
        self.__repo.modificare_pret(id,pret_nou)

    def importa(self,filename):
        return self.__repo.importa(filename)