import argparse
import time
import timeit
import functools

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

def ejecutarAlgoritmo(func, nElementos, nVeces, detalle):
    
    total = 0

    for i in range(0, nVeces):
        lista = generarLista(nElementos)
        inicio = time.time()
        func(lista.copy())
        fin = time.time()
        t = fin - inicio
        if(detalle):
            print("  - " + str(i) + ": " + "{:.3f}".format(t) + "s")
        total = total + t
    
    
    print(func.__name__ + ": " + "{:.3f}".format(total/nVeces) + "s")
    
    #t = timeit.Timer(functools.partial(func, lista))
    #res = t.timeit(10)
    #print(func.__name__ + ": " + "{:.3f}".format(res) + "s")

def pruebaAlgoritmo(func, lista):
    print(lista)
    func(lista)
    print(lista)

def ejecutarTodo():

    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--elementos", type=int, required=True)
    parser.add_argument("-v", "--veces", type=int, required=False, default=1)
    parser.add_argument("--lentos", required=False, action='store_true')
    parser.add_argument("--detalle", required=False, action='store_true')
    args = parser.parse_args()

    nElementos = args.elementos
    nVeces = args.veces
    detalle = args.detalle
    

    # pruebaAlgoritmo(radixsort_v1, lista)
    # exit()

    print("Ejecución de los distintos algoritmos " + str(nVeces) + " veces con listas de " + str(nElementos) + " elementos:")

    if(args.lentos):
        ejecutarAlgoritmo(bubblesort, nElementos, nVeces, detalle)
        ejecutarAlgoritmo(selectsort, nElementos, nVeces, detalle)
        ejecutarAlgoritmo(insertsort, nElementos, nVeces, detalle)
    else:
        ejecutarAlgoritmo(mergesort_v1, nElementos, nVeces, detalle)
        ejecutarAlgoritmo(mergesort_v2, nElementos, nVeces, detalle)
        ejecutarAlgoritmo(mergesort_v3, nElementos, nVeces, detalle)
        ejecutarAlgoritmo(quicksort, nElementos, nVeces, detalle)
        ejecutarAlgoritmo(radixsort_v1, nElementos, nVeces, detalle)
        ejecutarAlgoritmo(radixsort_v2, nElementos, nVeces, detalle)


if __name__ == '__main__':
    ejecutarTodo()