from ordenacion.utils import swap

def bubblesort(lista):

    for i in range(len(lista) - 1, -1, -1):
        for j in range(0, i):
            if(lista[j] > lista[j+1]):
                swap(lista, j, j + 1)