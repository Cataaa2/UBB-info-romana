lista = [1,2,3,4]

def numere_negative(l):
    if len(l) == 1:
        if l[0] < 0:
            return 1
        else:
            return 0
    m = len(l) // 2
    st = l[:m]
    dr = l[m:]
    return numere_negative(st) + numere_negative(dr)

def maxim_lista(l):
    if len(l) == 1:
        return l[0]
    m = len(l)//2
    st = l[:m]
    dr = l[m:]
    m1 = maxim_lista(st)
    m2 = maxim_lista(dr)
    if m1>m2:
        return m1
    return m2

def inversare(l):
    if len(l) == 1:
        return l
    m = len(l) // 2
    st = l[:m]
    dr = l[m:]
    return inversare(dr) + inversare(st)

def produs_prozitii_pare(l,start=0):
    if len(l) == 0:
        return 1
    if len(l) == 1:
        if start%2==0:
            return l[0]
        else:
            return 1

    m = len(l)//2
    st = l[:m]
    dr = l[m:]
    return produs_prozitii_pare(st,start) * produs_prozitii_pare(dr,start+m)


# rez = produs_prozitii_pare(lista)
# print(rez)

def fara_pare(l):
    if len(l) == 1:
        if l[0] %2 != 0:
            return [l[0]]
        else:
            return []
    m = len(l)//2
    st = l[:m]
    dr = l[m:]
    return fara_pare(st)+fara_pare(dr)

rez = fara_pare(lista)
print(rez)