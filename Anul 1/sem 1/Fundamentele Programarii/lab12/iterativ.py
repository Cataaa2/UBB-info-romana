lista = [4,7,2,3,1,5]

def solutie(x):
    return len(x) > 0

def sub_secvente_iterativ(lista):
    n = len(lista)
    stiva = [(0,[])]
    rezultate = []
    while stiva:
        start, secv = stiva.pop()

        if solutie(secv):
            rezultate.append(secv)

        for i in range(n-1,start-1,-1):
            if not secv or lista[i] > secv[-1]:
                secv_noua = secv + [lista[i]]
                stiva.append((i+1,secv_noua))

    return rezultate

rezultate = sub_secvente_iterativ(lista)
print(rezultate)