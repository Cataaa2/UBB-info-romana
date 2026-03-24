elemente = [1,6,9,11,50,51,52]

def cautare_binara_iterativ(el,l):
    if len(l) == 0:
        return 0
    if el <= l[0]:
        return 0
    if el > l[-1]:
        return len(l)

    st = 0
    dr = len(l)-1
    while st <= dr:
        m = (st+dr)//2
        if el <= l[m]:
            dr = m-1
        else:
            st = m+1
    return st

# rez = cautare_binara_iterativ(11,elemente)
# print(rez)

def caut_bin_rec(el,l,st,dr):
    if st > dr:
        return st

    m = (st+dr)//2
    if el == l[m]:
        return m
    if el < l[m]:
        return caut_bin_rec(el,l,st,m-1)
    else:
        return caut_bin_rec(el,l,m+1,dr)

def cautare_binara_rec(el,l):
    if len(l) == 0:
        return 0
    if el <= l[0]:
        return 0
    if el > l[-1]:
        return len(l)
    return caut_bin_rec(el,l,0,len(l)-1)

# rez = cautare_binara_rec(9,elemente)
# print(rez)