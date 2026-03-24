def mergesort(arr):
    if len(arr)<=1:
        return arr

    mijloc = len(arr) // 2
    stanga = mergesort(arr[:mijloc])
    dreapta = mergesort(arr[mijloc:])

    return merge(stanga,dreapta)

def merge(st,dr):
    lista_sortata = []
    i = 0
    j = 0
    while i<len(st) and j<len(dr):
        if st[i] < dr[j]:
            lista_sortata.append(st[i])
            i = i+1
        else:
            lista_sortata.append(dr[j])
            j = j+1

    while i<len(st):
        lista_sortata.append(st[i])
        i += 1

    while j<len(dr):
        lista_sortata.append(dr[j])
        j += 1

    return lista_sortata

numere = [64, 25, 12, 22, 11,8,4,5,7,3]
rez = mergesort(numere)
print(rez)