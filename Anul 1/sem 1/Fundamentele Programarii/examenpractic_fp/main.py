from UI.consola import Consola
from controller.service import Service
from repository.repo_sedinte import Repository
from validator.validator_sedinte import Validator

repo_sedinte = Repository("sedinte.txt")
validator = Validator
service = Service(repo_sedinte,validator)
ui = Consola(service)

ui.run()