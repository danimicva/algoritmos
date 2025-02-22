#ifndef _SORT_H_
#define _SORT_H_

#define N_ALGORITMOS 3

#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <string.h>
#include "lista.h"
#include "bubblesort.h"
#include "mergesort.h"
#include "insertionsort.h"

typedef struct Ejecucion{
    char *algoritmo;
    long tiempo;
    int tamanoLista;
    long comparaciones;
    long accesosArray;
    long memoriaReservada;
    long objetosAlojados;
    long objetosLiberados;
    int correcto;
}Ejecucion;


Ejecucion *ejecutaAlgoritmoMucho(int tamInicial, int intervalo, int nEjecuciones);


#endif
