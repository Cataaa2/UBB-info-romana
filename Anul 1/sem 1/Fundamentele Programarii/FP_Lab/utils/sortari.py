def bubble_sort(lista, key=None, reverse=False, cmp=None):
    """
    Sorteaza lista folosind metoda Bubble Sort.
    """
    n = len(lista)
    schimbat = True
    while schimbat:
        schimbat = False
        for i in range(n - 1):
            ele1 = lista[i]
            ele2 = lista[i + 1]

            val1 = key(ele1) if key else ele1
            val2 = key(ele2) if key else ele2
            should_swap = False

            if cmp:
                if cmp(val1, val2) > 0:
                    should_swap = True
            else:
                if val1 > val2:
                    should_swap = True

            if reverse and cmp is None:
                if val1 < val2:
                    should_swap = True
                else:
                    should_swap = False
            elif reverse and cmp:
                if cmp(val1, val2) < 0:
                    should_swap = True

            if should_swap:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                schimbat = True

def shell_sort(lista, key=None, reverse=False, cmp=None):
    """
    Sorteaza lista folosind metoda Shell Sort.
    Complexitate medie: O(n log n)
    """
    n = len(lista)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            val_temp = key(temp) if key else temp
            j = i
            while j >= gap:
                ele_gap = lista[j - gap]
                val_gap = key(ele_gap) if key else ele_gap
                should_swap = False
                if cmp:
                    if cmp(val_gap, val_temp) > 0:
                        should_swap = True
                else:
                    if val_gap > val_temp:
                        should_swap = True

                if reverse:
                    should_swap = False
                    if cmp:
                        if cmp(val_gap, val_temp) < 0:
                            should_swap = True
                    else:
                        if val_gap < val_temp:
                            should_swap = True
                if should_swap:
                    lista[j] = lista[j - gap]
                    j -= gap
                else:
                    break
            lista[j] = temp
        gap //= 2


def sortare_generica(lista, key=None, reverse=False, algoritm='shell', cmp=None):
    """
    Functie care apeleaza algoritmul dorit.
    algoritm poate fi: 'bubble' sau 'shell'
    """
    if algoritm == 'bubble':
        bubble_sort(lista, key, reverse, cmp)
    elif algoritm == 'shell':
        shell_sort(lista, key, reverse, cmp)
    else:
        #sortarea nativa daca algoritmul nu e recunoscut
        lista.sort(key=key, reverse=reverse)