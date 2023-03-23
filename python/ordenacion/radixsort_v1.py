def radixsort_v1(lista):
    width = len(str(max(lista)))
    lista2 = radixsort_v1_int(lista, 0, width)
    
    for i in range(0, len(lista)):
        lista[i] = lista2[i]

def radixsort_v1_int(lista, idx, width):
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

    
    L0 = radixsort_v1_int(dic[0], idx + 1, width) if len(dic[0]) > 0 else []
    L1 = radixsort_v1_int(dic[1], idx + 1, width) if len(dic[1]) > 0 else []
    L2 = radixsort_v1_int(dic[2], idx + 1, width) if len(dic[2]) > 0 else []
    L3 = radixsort_v1_int(dic[3], idx + 1, width) if len(dic[3]) > 0 else []
    L4 = radixsort_v1_int(dic[4], idx + 1, width) if len(dic[4]) > 0 else []
    L5 = radixsort_v1_int(dic[5], idx + 1, width) if len(dic[5]) > 0 else []
    L6 = radixsort_v1_int(dic[6], idx + 1, width) if len(dic[6]) > 0 else []
    L7 = radixsort_v1_int(dic[7], idx + 1, width) if len(dic[7]) > 0 else []
    L8 = radixsort_v1_int(dic[8], idx + 1, width) if len(dic[8]) > 0 else []
    L9 = radixsort_v1_int(dic[9], idx + 1, width) if len(dic[9]) > 0 else []
    
    return L0 + L1 + L2 + L3 + L4 + L5 + L6 + L7 + L8 + L9
