studenti = []
probleme = []

def creeaza_student(id,nume,grup):
    return {
        'id':id,
        'nume':nume,
        'grup':grup
    }

def get_id(student):
    return student['id']

def get_nume(student):
    return student['nume']

def get_grup(student):
    return student['grup']

def creeaza_problema(nrlab, nrproblema, descriere, deadline):
    return {
        'nrlab': nrlab,
        'nrproblema': nrproblema,
        'descriere': descriere,
        'deadline': deadline
    }

def get_nrlab(problema):
    return problema['nrlab']

def get_nrproblema(problema):
    return problema['nrproblema']

def get_descriere(problema):
    return problema['descriere']

def get_deadline(problema):
    return problema['deadline']