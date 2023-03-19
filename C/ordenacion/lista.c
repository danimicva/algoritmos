#include "lista.h"

int *generaLista(int tamano){

  int *lista;
  
  lista = (int *) malloc(sizeof(int) * tamano);
  if(lista == NULL){
    return NULL;
  }
  
  for(int i = 0; i < tamano; i++){
    lista[i] = rand() % tamano;
  }
  
  return lista;
  
}

void liberarLista(int *l){
  free(l);
}

int getElemento(int *lista, int n){
  return lista[n];
}

void setElemento(int *lista, int pos,  int dato){
  lista[pos] = dato;
}

void imprimeLista(int *lista, int n){

  printf("Lista: \n");
  printf("Tamaño: %d\n", n);
  printf("Elementos: \n");

  for(int i = 0; i < n; i++){
    printf(" - %d\n", lista[i]);
  }
}

void copiaLista(int *lista1, int *lista2, int n){
  
  for(int i=0; i < n; i++){
    lista2[i] = lista1[i];
  }
  
  return;
}

int comprobarLista(int *lista, int tam){

  for(int i = 1; i < tam; i++){
    if(lista[i - 1] > lista[i]){
      return -1;
    }
  }

  return 0;
}

void swap(int *lista, int pos1, int pos2){
  int temp = lista[pos1];
  lista[pos1] = lista[pos2];
  lista[pos2] = temp;
}
