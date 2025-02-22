#ifndef _LISTA_H_
#define _LISTA_H_

#include <stdio.h>
#include <stdlib.h>


int *crearLista(int tamano);
void liberarLista(int *l);
int getElemento(int *lista, int n);
void setElemento(int *lista, int pos, int dato);
void imprimeLista(int *lista, int n);

int *generaLista(int n);
void copiaLista(int *lista1, int *lista2, int n);
int comprobarLista(int *lista, int tam);

void swap(int *lista, int pos1, int pos2);

#endif