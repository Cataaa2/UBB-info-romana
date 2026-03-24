def selection_sort(l):
    n = len(l)
    for i in range(n-1):
        index_min = i
        for j in range(i+1,n):
            if l[j] < l[index_min]:
                index_min = j
        if index_min != i:
            l[i], l[index_min] = l[index_min], l[i]
numere = [64, 25, 12, 22, 11]
selection_sort(numere)
print(numere)
