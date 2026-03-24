def is_prime(x):
    d = 0
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            d += 1
    if d != 0:
        return False
    return True

def sub_prime_cresc(arr):
    n = len(arr)
    dp = [0] * n
    prev = [-1] * n
    max_len = 0
    index_global = -1
    for i in range(n):
        if not is_prime(arr[i]):
            continue
        dp[i] = 1
        for j in range(i):
            if is_prime(arr[j]) and arr[j] < arr[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j]+1
                    prev[i] = j

        if dp[i] > max_len:
            max_len = dp[i]
            index_global = i

    sol = []
    curent = index_global
    while curent != -1:
        sol.append(arr[curent])
        curent = prev[curent]

    return sol[::-1]

lista1 = [21,2,11,3,4,7,13]
rez = sub_prime_cresc(lista1)
print(rez)

def pare_desc(arr):
    n = len(arr)
    dp = [0] * n
    prev = [-1] * n
    max_len = 0
    index_final = -1
    for i in range(n):
        if arr[i] % 2 != 0:
            continue
        dp[i] = 1
        for j in range(i):
            if arr[j]>arr[i] and arr[j] % 2==0:
                if dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
                    prev[i] = j
        if dp[i] > max_len:
            max_len = dp[i]
            index_final = i

    sol = []
    curent = index_final
    while curent != -1:
        sol.append(arr[curent])
        curent = prev[curent]

    return sol[::-1]

lista2 = [2,12,3,6,14,3,4,7,2]
rez = pare_desc(lista2)
print(rez)
