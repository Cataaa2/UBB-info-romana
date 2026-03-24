from domeniu_modular import studenti, creeaza_student, creeaza_problema, probleme, get_id, get_nrlab,get_nrproblema


def adauga_student(id, nume, grup):
    for s in studenti:
        if get_id(s) == id:
            print("id student existent")
            return
    student_nou = creeaza_student(id, nume, grup)
    studenti.append(student_nou)

def adauga_problema(nrlab, nrprob, descriere, deadline):
    for p in probleme:
        if get_nrlab(p) == nrlab and get_nrproblema(p) == nrprob:
            print("Problema exista deja")
            return
    problema_noua = creeaza_problema(nrlab, nrprob, descriere, deadline)
    probleme.append(problema_noua)
    print("Problema adaugata")

