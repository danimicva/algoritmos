import random as rnd

def swap(lista, p1, p2):
    item2 = lista[p2]
    lista[p2] = lista[p1]
    lista[p1] = item2

def generarLista(n):

    lista = []

    for i in range(0, n):
        lista.append(rnd.randint(0, n))

    return lista
