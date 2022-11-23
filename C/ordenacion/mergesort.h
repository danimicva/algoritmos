#ifndef _MERGESORT_H_
#define _MERGESORT_H_


#include <stdio.h>
#include <stdlib.h>

long mergeSort(int *lista, int tam);
int mergeSortInterno(int *lista, int tam, long *comp);
int dividirLista(int *listaOrigen, int tamOrigen, int **lista1, int *tam1, int **lista2, int *tam2);

#endif
