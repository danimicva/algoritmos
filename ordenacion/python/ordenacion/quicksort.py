from ordenacion.utils import swap

def quicksort(lista):
    quicksort_int(lista, 0, len(lista) - 1)
        
def quicksort_int(lista, inicio, fin):

    if(fin <= inicio):
        return

    pivot = fin
    j = inicio
    
    for i in range(inicio, fin):
        if(lista[i] < lista[pivot]):
            while(lista[j] < lista[pivot] and j < i):
                j =+ 1
            if(i != j):
                swap(lista, i, j)
            j += 1
    
    swap(lista, j, pivot)

    quicksort_int(lista, inicio, j - 1)
    quicksort_int(lista, j + 1, fin)