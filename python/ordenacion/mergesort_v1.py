
def mergesort_v1(lista):

    merge_v1_int(lista, 0, len(lista))
    return


def merge_v1_int(lista, i1, i2):

    if(i2 - i1 <= 1):
        return
    medio = (i1+i2)//2
    merge_v1_int(lista, i1, medio)
    merge_v1_int(lista, medio, i2)
    merge_v1(lista, i1, medio, i2)

def merge_v1(lista, i1, i2, i3):

    L1 = []
    for i in range(i1, i2):
        L1.append(lista[i])

    L2 = []
    for i in range(i2, i3):
        L2.append(lista[i])

    ii1 = 0
    ii2 = 0
    iLista = i1
    while(ii1 < len(L1) and ii2 < len(L2)):
        if(L1[ii1] < L2[ii2]):
            lista[iLista] = L1[ii1]
            ii1 = ii1 + 1
        else:
            lista[iLista] = L2[ii2]
            ii2 = ii2 + 1
        iLista = iLista + 1


    while(ii1 < len(L1)):
        lista[iLista] = L1[ii1]
        ii1 = ii1 + 1
        iLista = iLista + 1

    while(ii2 < len(L2)):
        lista[iLista] = L2[ii2]
        ii2 = ii2 + 1
        iLista = iLista + 1
