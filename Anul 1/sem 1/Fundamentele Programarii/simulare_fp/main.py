from UI.consola import Consola
from controller.service_carti import ServiceCarti
from infrastructura.repo_carti import RepositoryCarti

fisier_carti = r"C:\Users\Catalin\PycharmProjects\simulare_fp\carti.txt"
repo_carti = RepositoryCarti(fisier_carti)
service_carti = ServiceCarti(repo_carti)

ui = Consola(service_carti)

ui.run()