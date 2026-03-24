import unittest

from controller.service import Service
from domain.sedinta import Sedinta
from exceptii.eroare_repo import EroareRepo
from exceptii.eroare_validator import EroareValidator
from repository.repo_sedinte import Repository
from validator.validator_sedinte import Validator


class Teste(unittest.TestCase):
    def setUp(self):
        self.repo = Repository("fisier_test.txt")
        self.validator = Validator
        self.service = Service(self.repo,self.validator)

    def tearDown(self):
        with open("fisier_test.txt",'w') as f:
            f.write("20.02,08:00,scoala,normal\n21.02,09:00,fotbal,extraordinar\n21.02,10:00,politica,normal\n")

    def test_get_all_sedinte_service(self):
        sedinte = self.service.get_all_sedinte()
        self.assertEqual(len(sedinte), 3)

    def test_get_all_sedinte_repo(self):
        sedinte = self.repo.get_all_sedinte()
        self.assertEqual(len(sedinte), 3)


#       TESTUL ASTA ESTE CORECT PENTRU DATA IN CARE A FOST SCRIS. PENTRU A FUNCTIONA TREBUIE ACTUALIZATE DATELE SEDINTELOR
#    def test_sedinte_ziua_urmatoare(self):
#        s1 = Sedinta("05.02", "09:15", "ceva1", "normal")
#        s2 = Sedinta("05.02", "10:30", "ceva2", "normal")
#        s3 = Sedinta("05.02", "07:00", "ceva3", "normal")
#        self.service.add(s1)
#        self.service.add(s2)
#        self.service.add(s3)
#        sedinte_ziua_urmatoare = self.service.get_sedinte_ziua_urmatoare()
#        self.assertEqual(len(sedinte_ziua_urmatoare),3)
#        self.assertEqual(sedinte_ziua_urmatoare[0].get_ora(),"07:00")
#        self.assertEqual(sedinte_ziua_urmatoare[1].get_ora(),"09:15")
#        self.assertEqual(sedinte_ziua_urmatoare[2].get_ora(),"10:30")

    def test_add(self):
        sedinta_noua = Sedinta("10.10", "09:00", "ceva", "normal")
        sedinte = self.repo.get_all_sedinte()
        self.assertEqual(len(sedinte),3)
        self.service.add(sedinta_noua)
        sedinte = self.repo.get_all_sedinte()
        self.assertEqual(len(sedinte), 4)

    def test_export(self):
        self.service.export("export_test.txt","al")
        self.repo2 = Repository("export_test.txt")
        sedinte_exportate = self.repo2.get_all_sedinte()
        self.assertEqual(len(sedinte_exportate),2)

    def test_sedinte_urmatoarele3_zile(self):
        s1 = Sedinta("05.06", "09:15", "ceva1", "normal")
        s2 = Sedinta("06.06", "10:30", "ceva2", "normal")
        s3 = Sedinta("07.06", "07:00", "ceva3", "normal")
        self.service.add(s1)
        self.service.add(s2)
        self.service.add(s3)
        self.service.set_filtru_data("04.06")
        filtrate = self.service.get_urm_3zile()
        self.assertEqual(len(filtrate),3)
        self.assertEqual(filtrate[0].get_data(),"05.06")
        self.assertEqual(filtrate[1].get_data(),"06.06")
        self.assertEqual(filtrate[2].get_data(),"07.06")


    def test_validator(self):
        sedinta_noua = Sedinta("99.99","88:88","","")
        self.assertRaises(EroareValidator,self.validator.valideaza_sedinta,sedinta_noua)
