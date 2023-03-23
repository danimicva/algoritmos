import argparse
import time

from ordenacion.utils import generarLista
from ordenacion.mergesort_v1 import mergesort_v1
from ordenacion.mergesort_v2 import mergesort_v2
from ordenacion.mergesort_v3 import mergesort_v3
from ordenacion.quicksort import quicksort
from ordenacion.bubblesort import bubblesort
from ordenacion.selectsort import selectsort
from ordenacion.insertsort import insertsort
from ordenacion.radixsort_v1 import radixsort_v1
from ordenacion.radixsort_v2 import radixsort_v2

def ejecutarAlgoritmo(func, lista):
    inicio = time.time()
    func(lista)
    fin = time.time()
    print(func.__name__ + ": " + "{:.3f}".format(fin - inicio) + "s")

def pruebaAlgoritmo(func, lista):
    print(lista)
    func(lista)
    print(lista)

def ejecutarTodo():

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int)
    parser.add_argument("--tambienLentos", required=False, action='store_true')
    args = parser.parse_args()

    lista = generarLista(args.n, 0, args.n)

    # pruebaAlgoritmo(radixsort_v1, lista)
    # exit()

    print("Ejecución de los distintos algoritmos con listas de " + str(args.n) + " elementos:")

    if(args.tambienLentos):
        ejecutarAlgoritmo(bubblesort, lista.copy())
        ejecutarAlgoritmo(selectsort, lista.copy())
        ejecutarAlgoritmo(insertsort, lista.copy())

    ejecutarAlgoritmo(mergesort_v1, lista.copy())
    ejecutarAlgoritmo(mergesort_v2, lista.copy())
    ejecutarAlgoritmo(mergesort_v3, lista.copy())
    ejecutarAlgoritmo(quicksort, lista.copy())
    ejecutarAlgoritmo(radixsort_v1, lista.copy())
    ejecutarAlgoritmo(radixsort_v2, lista.copy())


if __name__ == '__main__':
    ejecutarTodo()