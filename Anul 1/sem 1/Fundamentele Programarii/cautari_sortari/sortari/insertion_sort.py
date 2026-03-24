def insertion_sort(l):
    for i in range(1,len(l)):
        el_curent = l[i]
        j = i-1
        while j>=0 and el_curent < l[j]:
            l[j+1] = l[j]
            j = j-1
        l[j+1] = el_curent

numere = [64, 25, 12, 22, 11]
insertion_sort(numere)
print(numere)
