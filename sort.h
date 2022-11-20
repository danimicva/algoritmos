#ifndef _SORT_H_
#define _SORT_H_

#define N_ALGORITMOS 3

#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <string.h>
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

typedef struct Lista{
	int *lista;
	int tamano;
}Lista;

Ejecucion *ejecutaAlgoritmoMucho(int tamInicial, int tamFinal, int intervalo);
Ejecucion *ejecutaAlgoritmos(int tamanoLista);
Ejecucion *ejecutaMergeSort(int *lista, int tam);
Ejecucion *ejecutaBubbleSort(Lista lista, int tam);
Ejecucion *ejecutaInsertionSort(Lista lista, int tam);
Lista *generaLista(int n);
Lista *copiaLista(Lista lista);
int comprobarLista(Lista lista);
void *reservarMemoria(int tamano);
void liberarMemoria(void *obj);
void swap(Lista *lista, int index1, int index2);
int getElemento(Lista *lista, int n);
int comparaElementos(Lista lista, int index1, int index2, char comp);
int comparaElementosEntreListas(Lista lista1, int index1, Lista lista2, int index2, char comp);

#endif
