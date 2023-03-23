from ordenacion.utils import swap

def insertsort(lista):

    for i in range(1, len(lista)):
        if(lista[i] < lista[i - 1]):
            j = i
            while(lista[j] < lista[j - 1] and j > 0):
                swap(lista, j, j  - 1)
                j = j - 1