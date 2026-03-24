import unittest

from controller.service import Service
from domain.produs import Produs
from Repository.repo_produse import RepositoryProduse

class Teste(unittest.TestCase):
    def setUp(self):
        self.repo = RepositoryProduse("fisier_test.txt")
        self.service = Service(self.repo)

    def tearDown(self):
        with open("fisier_test.txt",'w') as f:
            f.write("1,lapte,5.89")

    def test_produs(self):
        produs = Produs(1,"lapte",5.89)
        self.assertEqual(produs.get_id(),1)
        self.assertEqual(produs.get_denumire(),"lapte")
        self.assertEqual(produs.get_pret(),5.89)

    def test_get_all_produse(self):
        produse = self.repo.get_all_produse()
        self.assertEqual(len(produse),1)

    def test_adaugare_produs(self):
        self.repo.adauga_produs(2,"bomboana",0.4)
        produse = self.repo.get_all_produse()
        self.assertEqual(len(produse), 2)
        self.assertEqual(produse[1].get_id(),2)
        self.assertEqual(produse[1].get_denumire(),"bomboana")
        self.assertEqual(produse[1].get_pret(),0.4)

    def test_sterge_dupa_cifra(self):
        self.repo.sterge_produse_dupa_cifra("5")
        produse = self.repo.get_all_produse()
        self.assertEqual(len(produse), 1)
        self.repo.sterge_produse_dupa_cifra("1")
        produse = self.repo.get_all_produse()
        self.assertEqual(len(produse), 0)

    def test_undo(self):
        self.repo.adauga_produs(2, "bomboana", 0.4)
        self.assertEqual(len(self.repo.get_all_produse()), 2)
        self.service.sterge_produse_dupa_cifra("1")
        self.service.sterge_produse_dupa_cifra("2")
        self.assertEqual(len(self.repo.get_all_produse()), 0)
        self.service.undo()
        self.assertEqual(len(self.repo.get_all_produse()), 1)
        self.service.undo()
        self.assertEqual(len(self.repo.get_all_produse()), 2)



