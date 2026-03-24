from Repository.repo_produse import RepositoryProduse
from UI.consola import Consola
from controller.service import Service

repo = RepositoryProduse("produse.txt")
service = Service(repo)
ui = Consola(service)

ui.run()