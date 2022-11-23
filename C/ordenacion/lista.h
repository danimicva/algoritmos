#ifndef _LISTA_H_
#define _LISTA_H_

#include <stdio.h>
#include <stdlib.h>

typedef struct Lista{
	int *lista;
	int tamano;
}Lista;

Lista *crearLista(int tamano);
void liberarLista(Lista *l);
int getTamano(Lista lista);
int getElemento(Lista lista, int n);
int setElemento(Lista lista, int pos, int dato);
void imprimeLista(Lista lista);

#endif