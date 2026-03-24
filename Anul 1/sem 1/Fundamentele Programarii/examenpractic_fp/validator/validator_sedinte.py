from exceptii.eroare_validator import EroareValidator


class Validator:
    def __init__(self):
        pass

    def valideaza_sedinta(sedinta):
        """
        functie care valideaza o sedinta
        raises EroareValidator daca sedinta nu este valida
        """
        erori = ""
        data = sedinta.get_data()
        ora = sedinta.get_ora()
        subiect = sedinta.get_subiect()
        fel = sedinta.get_fel()
        ok = False
        try:
            parti_data = data.split(".")
            if len(parti_data) != 2:
                raise ValueError
            ok = True
        except ValueError:
            erori += "format data invalid (trebuie dd.mm)\n"
        if ok:
            zi_sedinta = int(parti_data[0])
            luna_sedinta = int(parti_data[1])
            if zi_sedinta<1 or zi_sedinta>28:
                erori += "zi invalida\n"
            if luna_sedinta<1 or luna_sedinta>12:
                erori += "luna invalida\n"
        ok = False
        try:
            parti_ora = ora.split(":")
            if len(parti_ora) != 2:
                raise ValueError
            ok = True
        except ValueError:
            erori += "format ora invalid (trebuie hh:mm)\n"
        if ok:
            ore_bune =["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
            min_bune = list(range(0,60))
            hh = parti_ora[0]
            mm = int(parti_ora[1])
            if hh not in ore_bune:
                erori += "ora invalida\n"
            if mm not in min_bune:
                erori += "minute invalide\n"
        if subiect == "":
            erori += "subiectul nu poate fi gol\n"
        feluri_bune = ["normal", "extraordinar"]
        if fel not in feluri_bune:
            erori += "felul trebuie sa fie normal sau extraodrinar\n"
        if len(erori)!=0:
            raise EroareValidator(erori)
