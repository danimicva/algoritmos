def mergesort_v2(lista):
    
    merge_v2_int(lista, 0, len(lista))
    return


def merge_v2_int(lista, i1, i2):

    if(i2 - i1 <= 1):
        return
    medio = (i1+i2)//2
    merge_v2_int(lista, i1, medio)
    merge_v2_int(lista, medio, i2)
    merge_v2(lista, i1, medio, i2)

def merge_v2(lista, i1, i2, i3):

    tmp = [None] * (i3 - i1)
    
    ii1 = 0
    ii2 = 0
    iLista = 0
    while(ii1 < i2-i1 and ii2 < i3-i2):
        if(lista[ii1+i1] < lista[ii2+i2]):
            tmp[iLista] = lista[ii1+i1]
            ii1 = ii1 + 1
        else:
            tmp[iLista] = lista[ii2+i2]
            ii2 = ii2 + 1
        iLista = iLista + 1


    while(ii1 < i2-i1):
        tmp[iLista] = lista[ii1+i1]
        ii1 = ii1 + 1
        iLista = iLista + 1

    while(ii2 < i3-i2):
        tmp[iLista] = lista[ii2+i2]
        ii2 = ii2 + 1
        iLista = iLista + 1

    for i in range(0, len(tmp)):
        lista[i1 + i] = tmp[i]
