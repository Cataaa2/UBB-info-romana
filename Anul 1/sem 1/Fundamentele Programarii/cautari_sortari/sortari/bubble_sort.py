def bubble_sort(l):
    n = len(l)
    for i in range(1,n):
        for j in range(n-i):
            if l[j]>l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

numere = [64, 25, 12, 22, 11]
bubble_sort(numere)
print(numere)