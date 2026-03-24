import unittest

from controller.service_carti import ServiceCarti
from exceptii.eroare_repo import EroareRepo
from infrastructura.repo_carti import RepositoryCarti


class Teste(unittest.TestCase):
    """
    Clasa pentru functii de test
    """
    def setUp(self):
        """
        Functie care pregateste Service-ul si Repository-ul pentru teste
        """
        self.__fisier_test = r"C:\Users\Catalin\PycharmProjects\simulare_fp\carti.txt"
        self.__repo_carti = RepositoryCarti(self.__fisier_test)
        self.__service_carti = ServiceCarti(self.__repo_carti)

    def test_cauta_dupa_autor(self):
        """
        Test cautare dupa autor
        """
        autor = "Liviu Rebreanu"
        carti = self.__service_carti.find_by_autor(autor)
        self.assertTrue(len(carti) == 2)
        for pseudo_isbn in carti:
            carte = carti[pseudo_isbn]
            self.assertTrue(carte.get_autor() == autor)
        autor = "abcd"
        carti = self.__service_carti.find_by_autor(autor)
        self.assertTrue(len(carti) == 0)

    def test_imprumuta_carte(self):
        """
        Test imprumutare carte
        """
        imprumut = self.__service_carti.imprumuta_carte("A123",10)
        carte = imprumut[0]
        self.assertTrue(carte.get_pseudo_isbn() == "A123")
        pret_total = 10 * int(carte.get_pret_pe_zi())
        self.assertTrue(pret_total == imprumut[1])
        pseudo_isbn_inexistent = "abcd"
        self.assertRaises(EroareRepo,self.__service_carti.imprumuta_carte,pseudo_isbn_inexistent,10)

