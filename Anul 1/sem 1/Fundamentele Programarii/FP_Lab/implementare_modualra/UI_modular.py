from domeniu_modular import *
from implementare_modualra.adaugare_modular import adauga_student, adauga_problema
from implementare_modualra.functionalitati_modular import sterge_student, sterge_problema


def cit_id():
    while True:
        try:
            id = int(input("id student: "))
            if id < 0:
                raise ValueError("id invalid")
            return id
        except ValueError:
            print("id invalid")

def cit_nume():
    while True:
        nume = input("nume: ").strip()
        if nume == "":
            print("numele nu poate fi gol")
        else:
            return nume

def cit_grup():
    while True:
        try:
            grup = int(input("grup student: "))
            if grup < 0:
                raise ValueError
            return grup
        except ValueError:
            print("grup invalid")

def citire_student():
    id = cit_id()
    nume = cit_nume()
    grup = cit_grup()
    return id,nume,grup

def cit_nrlab():
    while True:
        try:
            nrlab = int(input("nr lab: "))
            if nrlab < 0:
                raise ValueError
            return nrlab
        except ValueError:
            print("nr lab invalid")

def cit_nrprob():
    while True:
        try:
            nrprob = int(input("nr problema: "))
            if nrprob < 0:
                raise ValueError
            return nrprob
        except ValueError:
            print("nr problema invalid")

def cit_descriere():
    while True:
        descriere = input("descriere: ").strip()
        if descriere == "":
            print("descrierea nu poate fi goala")
        else:
            return descriere

def cit_deadline():
    while True:
        try:
            deadline = int(input("deadline: "))
            if deadline < 0:
                raise ValueError
            return deadline
        except ValueError:
            print("deadline invalid")

def citire_problema():
    nrlab = cit_nrlab()
    nrprob = cit_nrprob()
    descriere = cit_descriere()
    deadline = cit_deadline()
    return nrlab,nrprob,descriere,deadline

def sterge_student_ui():
    id = cit_id()
    sterge_student(id)

def sterge_problema_ui():
    nrlab = cit_nrlab()
    nrprob = cit_nrprob()
    sterge_problema(nrlab,nrprob)

def afiseaza_studentii():
    if len(studenti) != 0:
        for s in studenti:
            print(f"id: {get_id(s)}, nume: {get_nume(s)}, grup: {get_grup(s)} ")
    else:
        print("nu aveti studenti")

def afiseaza_probleme():
    if len(probleme) != 0:
        for p in probleme:
            print(f"{get_nrlab(p)}_{get_nrproblema(p)}, {get_descriere(p)}, deadline: {get_deadline(p)} zile")
    else:
        print("nu aveti probleme")

def printMenu():
    print("1. adauga student")
    print("2. adauga problema")
    print("3. afiseaza studentii")
    print("4. afiseaza problemele")
    print("5. sterge student")
    print("6. sterge problema")
    print("0. exit")

def run():
    studenti.clear()
    probleme.clear()
    finish = False
    while not finish:
        printMenu()
        opt = input(">>>").strip()
        if opt == '0':
            finish = True
            print("bye")
        elif opt == '1':
            id, nume, grup = citire_student()
            adauga_student(id,nume,grup)
        elif opt == '2':
            nrlab, nrproblema, descriere, deadline = citire_problema()
            adauga_problema(nrlab,nrproblema,descriere,deadline)
        elif opt == '3':
            afiseaza_studentii()
        elif opt == '4':
            afiseaza_probleme()
        elif opt == '5':
            sterge_student_ui()
        elif opt == '6':
            sterge_problema_ui()
        else:
            print("optiune invalida!")
