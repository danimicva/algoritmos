import argparse
import time
import random as rnd

swaps = 0
accesos = 0
escrituras = 0

def generarLista(n, min, max):

    lista = []

    for i in range(0, n):
        lista.append(rnd.randint(min, max))

    return lista


def swap(lista, p1, p2):
    item2 = lista[p2]
    lista[p2] = lista[p1]
    lista[p1] = item2
#    global swaps
#    swaps = swaps + 1

def acceder(lista, indice):
    global accesos
    accesos = accesos + 1
    return lista[indice]

def escribir(lista, indice, valor):
    lista[indice] = valor
    global escrituras
    escrituras = escrituras + 1

def bubblesort(lista):

    for i in range(len(lista) - 1, -1, -1):
        for j in range(0, i):
#            if(acceder(lista, j) > acceder(lista, j + 1)):
            if(lista[j] > lista[j+1]):
                swap(lista, j, j + 1)

    return 

def plomosort(lista):
    for i in range(0, len(lista) + 1):
        for j in range(len(lista) - 1, i, -1):
#            if(acceder(lista, j) < acceder(lista, j - 1)):
            if(lista[j] < lista[j - 1]):
                swap(lista, j, j - 1)

    return

def selectsort(lista):

    for j in range(0, len(lista)):
        menor = j
        for i in range(j + 1, len(lista)):
#            if(acceder(lista, i) < acceder(lista, menor)):
            if(lista[i] < lista[menor]):
                menor = i
        swap(lista, menor, j)

    return



def insertsort(lista):

    for i in range(1, len(lista)):
        if(lista[i] < lista[i - 1]):
            j = i
#            while(acceder(lista, j) < acceder(lista, j - 1) and j > 0):
            while(lista[j] < lista[j - 1] and j > 0):
                swap(lista, j, j  - 1)
                j = j - 1

def mergesort(lista):

    merge_int(lista, 0, len(lista))
    return


def merge_int(lista, i1, i2):

    if(i2 - i1 <= 1):
        return;
    medio = (i1+i2)//2
    merge_int(lista, i1, medio)
    merge_int(lista, medio, i2)
    merge(lista, i1, medio, i2)

def merge(lista, i1, i2, i3):

    L1 = []
    for i in range(i1, i2):
#       L1.append(acceder(lista, i))
        L1.append(lista[i])

    L2 = []
    for i in range(i2, i3):
#        L2.append(acceder(lista, i))
        L2.append(lista[i])

    ii1 = 0
    ii2 = 0
    iLista = i1
    while(ii1 < len(L1) and ii2 < len(L2)):
#        if(acceder(L1, ii1) < acceder(L2, ii2)):
        if(L1[ii1] < L2[ii2]):
#            escribir(lista, iLista, acceder(L1, ii1))
            lista[iLista] = L1[ii1]
            ii1 = ii1 + 1
        else:
#            escribir(lista, iLista, acceder(L2, ii2))
            lista[iLista] = L2[ii2]
            ii2 = ii2 + 1
        iLista = iLista + 1


    while(ii1 < len(L1)):
#        escribir(lista, iLista, acceder(L1, ii1))
        lista[iLista] = L1[ii1]
        ii1 = ii1 + 1
        iLista = iLista + 1

    while(ii2 < len(L2)):
#        escribir(lista, iLista, acceder(L2, ii2))
        lista[iLista] = L2[ii2]
        ii2 = ii2 + 1
        iLista = iLista + 1

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

def radixsort(lista, idx, width):

    if(idx > width - 1):
        return lista
    dic = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9:[]}
    
    for i in range(0, len(lista)):
        tmp = str(lista[i]).zfill(width) # formatear le número al número de 0 que hay???
        if(tmp[idx] == '0'):
            dic[0].append(lista[i])        
        elif(tmp[idx] == '1'):
            dic[1].append(lista[i])
        elif(tmp[idx] == '2'):
            dic[2].append(lista[i])
        elif(tmp[idx] == '3'):
            dic[3].append(lista[i])
        elif(tmp[idx] == '4'):
            dic[4].append(lista[i])
        elif(tmp[idx] == '5'):
            dic[5].append(lista[i])
        elif(tmp[idx] == '6'):
            dic[6].append(lista[i])
        elif(tmp[idx] == '7'):
            dic[7].append(lista[i])
        elif(tmp[idx] == '8'):
            dic[8].append(lista[i])
        elif(tmp[idx] == '9'):
            dic[9].append(lista[i])

    
    L0 = radixsort(dic[0], idx + 1, width) if len(dic[0]) > 0 else []
    L1 = radixsort(dic[1], idx + 1, width) if len(dic[1]) > 0 else []
    L2 = radixsort(dic[2], idx + 1, width) if len(dic[2]) > 0 else []
    L3 = radixsort(dic[3], idx + 1, width) if len(dic[3]) > 0 else []
    L4 = radixsort(dic[4], idx + 1, width) if len(dic[4]) > 0 else []
    L5 = radixsort(dic[5], idx + 1, width) if len(dic[5]) > 0 else []
    L6 = radixsort(dic[6], idx + 1, width) if len(dic[6]) > 0 else []
    L7 = radixsort(dic[7], idx + 1, width) if len(dic[7]) > 0 else []
    L8 = radixsort(dic[8], idx + 1, width) if len(dic[8]) > 0 else []
    L9 = radixsort(dic[9], idx + 1, width) if len(dic[9]) > 0 else []
    
    return L0 + L1 + L2 + L3 + L4 + L5 + L6 + L7 + L8 + L9

# Inicio

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int)
parser.add_argument("max", type=int)
args = parser.parse_args()

lista = generarLista(args.n, 0, args.max)

# inicio = time.time()
# bubblesort(lista.copy())
# fin = time.time()
# print("Bubblesort: " + str(fin - inicio))

# inicio = time.time()
# plomosort(lista.copy())
# fin = time.time()
# print("Plomosort: " + str(fin - inicio))

# inicio = time.time()
# selectsort(lista.copy())
# fin = time.time()
# print("Selectsort: " + str(fin - inicio))

# inicio = time.time()
# insertsort(lista.copy())
# fin = time.time()
# print("Insertsort: " + str(fin - inicio))

inicio = time.time()
mergesort(lista.copy())
fin = time.time()
print("Mergesort: " + str(fin - inicio))

inicio = time.time()
quicksort(lista.copy())
fin = time.time()
print("Quicksort: " + str(fin - inicio))

inicio = time.time()
ordenada = radixsort(lista.copy(), 0, len(str(args.max)))
fin = time.time()
print("Radixsort: " + str(fin - inicio))
