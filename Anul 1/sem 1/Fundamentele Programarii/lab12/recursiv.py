def sub_secvente(lista,secv,start,rezultat):
    if len(secv) >=1:
        rezultat.append(secv[:])

    for i in range(start,len(lista)):
        if not secv or lista[i] > secv[-1]:
                secv.append(lista[i])
                sub_secvente(lista,secv,i+1,rezultat)
                secv.pop()

def get_sub_secvente(lista):
    solutii=[]
    sub_secvente(lista,[],0,solutii)
    return solutii

lista = [4,7,2,3,1,5]
rezultate = get_sub_secvente(lista)
print(rezultate)