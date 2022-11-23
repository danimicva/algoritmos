#include "lista.h"

Lista *crearLista(int tamano){
  Lista *l;

  l = (Lista *)malloc(sizeof(Lista));
  if(!l){
    return NULL;
  }

  l->lista = (int *) malloc(sizeof(int) * tamano);
  if(!l->lista){
    return NULL;
  }

  l->tamano = tamano;

  return l;
}

void liberarLista(Lista *l){
  free(l->lista);
  free(l);
}

int getTamano(Lista lista){
  return lista.tamano;
}

int getElemento(Lista lista, int n){
  return lista.lista[n];
}

int setElemento(Lista lista, int pos,  int dato){
  lista.lista[pos] = dato;
}

void imprimeLista(Lista lista){

  int i;

  printf("Lista: \n");
  printf("Tamaño: %d\n", getTamano(lista));
  printf("Elementos: \n");

  for(i = 0;i<getTamano(lista); i++){
    printf(" - %d\n", getElemento(lista, i));
  }
}