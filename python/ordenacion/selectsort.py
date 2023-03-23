from ordenacion.utils import swap

def selectsort(lista):

    for j in range(0, len(lista)):
        menor = j
        for i in range(j + 1, len(lista)):
            if(lista[i] < lista[menor]):
                menor = i
        swap(lista, menor, j)