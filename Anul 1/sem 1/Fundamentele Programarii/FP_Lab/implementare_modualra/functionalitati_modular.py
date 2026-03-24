from domeniu_modular import studenti, probleme, get_id, get_nrlab, get_nrproblema


def sterge_student(id):
    global studenti
    initial_len = len(studenti)
    studenti = [s for s in studenti if get_id(s) != id]
    if len(studenti) < initial_len:
        print(f"Studentul cu ID {id} a fost sters.")
    else:
        print(f"Studentul cu ID {id} nu exista.")

def sterge_problema(nrlab, nrprob):
    global probleme
    initial_len = len(probleme)
    probleme = [p for p in probleme if not (get_nrlab(p) == nrlab and get_nrproblema(p) == nrprob)]
    if len(probleme) < initial_len:
        print(f"Problema {nrlab}_{nrprob} a fost stearsa.")
    else:
        print(f"Problema {nrlab}_{nrprob} nu exista.")



