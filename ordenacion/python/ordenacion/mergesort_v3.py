def mergesort_v3(lista):

    merge_v3_int(lista, 0, len(lista))
    return


def merge_v3_int(lista, i1, i2):

    if(i2 - i1 <= 1):
        return
    medio = (i1+i2)//2
    merge_v3_int(lista, i1, medio)
    merge_v3_int(lista, medio, i2)
    merge_v3(lista, i1, medio, i2)

def merge_v3(lista, i1, i2, i3):

    L1 = lista[i1:i2].copy()
    L2 = lista[i2:i3].copy()

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
