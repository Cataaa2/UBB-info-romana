def partition(arr,low,high):
    i = low - 1
    j = high + 1
    pivot = arr[low]
    while True:
        i += 1
        while arr[i]<pivot:
            i = i+1

        j -= 1
        while arr[j]>pivot:
            j = j-1

        if i>=j:
            return j
        arr[i],arr[j] = arr[j],arr[i]

def quicksortrec(arr,low,high):
    if low<high:
        pivot = partition(arr,low,high)
        quicksortrec(arr,low,pivot)
        quicksortrec(arr,pivot+1,high)

def quickSort(arr):
    quicksortrec(arr,0,len(arr)-1)

numere = [64, 25, 12, 22, 11,8,4,5,7,3]
quickSort(numere)
print(numere)