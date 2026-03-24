from exceptii.eroare_validator import EroareValidator


class ValidatorNota:

    def valideaza_nota(self,nota):
        erori = ""
        if nota is not None:
            if nota < 1.0 or nota >10.0:
                erori += "nota invalida\n"
        if len(erori) > 0:
            raise EroareValidator(erori)