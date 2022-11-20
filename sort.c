#include "sort.h"

Ejecucion *ejecutaAlgoritmoMucho(int tamInicial, int tamFinal, int intervalo){

  int i, j, k;
  int nEjs;
  Ejecucion *ejs;
  Ejecucion *temp;

  nEjs = tamFinal - tamInicial;

  ejs = (Ejecucion *) malloc(sizeof(Ejecucion) * N_ALGORITMOS * nEjs);
  if(ejs == NULL){
    printf("Error reservando memoria para las ejecuciones.\n");
    return NULL;
  }
 
  for(i = tamInicial, j = 0; i <= tamFinal; i += intervalo, j++){

  temp = ejecutaAlgoritmos(i);
    if(temp == NULL){
      free(ejs);
      printf("Error ejecutando algoritmos para tamaño: %d\n", i);
      return NULL;
    }

    for(k = 0; k < N_ALGORITMOS; k++){
      ejs[(j * N_ALGORITMOS) + k] = temp[k];
    }
    free(temp);
  }

  return ejs;

}

Ejecucion *ejecutaAlgoritmos(int tamanoLista){

  int *listaOrig;
  int *listaCopia;
  Ejecucion *ejs;
  Ejecucion *e;

  ejs = (Ejecucion *) malloc(sizeof(Ejecucion) * N_ALGORITMOS);
  if(ejs == NULL){
    printf("Error alojando memoria.\n");
    return NULL;
  }

  listaOrig = generaLista(tamanoLista);
  listaCopia = generaLista(tamanoLista);
  if(listaOrig == NULL || listaCopia == NULL){
    printf("Error generando las listas.\n");
    return NULL;
  }

 
  copiaLista(listaOrig, listaCopia, tamanoLista);
  e = ejecutaMergeSort(listaCopia, tamanoLista);
  if(e == NULL){
    free(listaOrig);
    free(listaCopia);
    printf("Error ejecutando mergesort.\n");
    return NULL;
  }
  ejs[0] = *e;
  printf("%15s: %10d %20ldns %20ld comp. %s\n", e->algoritmo, e->tamanoLista, e->tiempo, e->comparaciones, e->correcto?"ERROR":"OK");
  free(e);

  copiaLista(listaOrig, listaCopia, tamanoLista);
  e = ejecutaBubbleSort(listaCopia, tamanoLista);
  if(e == NULL){
    free(listaOrig);
    free(listaCopia);
    printf("Error ejecutando bubblesort.\n");
    return NULL;
  }
  printf("%15s: %10d %20ldns %20ld comp. %s\n", e->algoritmo, e->tamanoLista, e->tiempo, e->comparaciones, e->correcto?"ERROR":"OK");
  ejs[1] = *e;
  free(e);

  copiaLista(listaOrig, listaCopia, tamanoLista);
  e = ejecutaInsertionSort(listaCopia, tamanoLista);
  if(e == NULL){
    free(listaOrig);
    free(listaCopia);
    printf("Error ejecutando bubblesort.\n");
    return NULL;
  }
  printf("%15s: %10d %20ldns %20ld comp. %s\n", e->algoritmo, e->tamanoLista, e->tiempo, e->comparaciones, e->correcto?"ERROR":"OK");
  ejs[1] = *e;
  free(e);

 

  free(listaOrig);
  free(listaCopia);

  return ejs;
}

Ejecucion *ejecutaMergeSort(int *lista, int tam){

  struct timespec tstart={0,0}, tend={0,0};
  long comparaciones;
  Ejecucion *ejecucion;

  clock_gettime(CLOCK_MONOTONIC, &tstart);
  comparaciones = mergeSort(lista, tam);
  clock_gettime(CLOCK_MONOTONIC, &tend);

  if(comparaciones == -1){
    printf("Error mergesort.\n");
    return NULL;
  }

  ejecucion = (Ejecucion *) malloc(sizeof(Ejecucion));
  if(ejecucion == NULL){
    printf("Error alojando ejecucion.\n");
    return NULL;
  }

  ejecucion->algoritmo = "Merge sort";
  ejecucion->tamanoLista = tam;
  ejecucion->comparaciones = comparaciones;
  ejecucion->tiempo = (tend.tv_sec * 1000000000 + tend.tv_nsec) - (tstart.tv_sec * 1000000000 + tstart.tv_nsec);
  ejecucion->correcto = comprobarLista(lista, tam);
  return ejecucion;
}

Ejecucion *ejecutaBubbleSort(int *lista, int tam){;

  struct timespec tstart={0,0}, tend={0,0};
  long comparaciones;
  Ejecucion *ejecucion;

  clock_gettime(CLOCK_MONOTONIC, &tstart);
  comparaciones = bubbleSort(lista, tam);
  clock_gettime(CLOCK_MONOTONIC, &tend);

  if(comparaciones == -1){
    printf("Error bubblesort.\n");
    return NULL;
  }

  ejecucion = (Ejecucion *) malloc(sizeof(Ejecucion));
  if(ejecucion == NULL){
    printf("Error alojando ejecucion.\n");
    return NULL;
  }

  ejecucion->algoritmo = "Bubble sort";
  ejecucion->tamanoLista = tam;
  ejecucion->comparaciones = comparaciones;
  ejecucion->tiempo = (tend.tv_sec * 1000000000 + tend.tv_nsec) - (tstart.tv_sec * 1000000000 + tstart.tv_nsec);
  ejecucion->correcto = comprobarLista(lista, tam);
  return ejecucion;

}

Ejecucion *ejecutaInsertionSort(int *lista, int tam){;

  struct timespec tstart={0,0}, tend={0,0};
  long comparaciones;
  Ejecucion *ejecucion;

  clock_gettime(CLOCK_MONOTONIC, &tstart);
  comparaciones = insertionSort(lista, tam);
  clock_gettime(CLOCK_MONOTONIC, &tend);

  if(comparaciones == -1){
    printf("Error insertion.\n");
    return NULL;
  }

  ejecucion = (Ejecucion *) malloc(sizeof(Ejecucion));
  if(ejecucion == NULL){
    printf("Error alojando ejecucion.\n");
    return NULL;
  }

  ejecucion->algoritmo = "Insertion sort";
  ejecucion->tamanoLista = tam;
  ejecucion->comparaciones = comparaciones;
  ejecucion->tiempo = (tend.tv_sec * 1000000000 + tend.tv_nsec) - (tstart.tv_sec * 1000000000 + tstart.tv_nsec);
  ejecucion->correcto = comprobarLista(lista, tam);
  return ejecucion;

}

int *generaLista(int n){

  int *lista;
  int i;
  
  lista = (int *) malloc(sizeof(int) * n);
  if(lista == NULL){
    return NULL;
  }
  
  for(i = 0; i<n; i++){
    lista[i] = rand() % n;
  }
  
  return lista;
  
}

void copiaLista(int *lista1, int *lista2, int tam){
  
  int i;
  
  for(i=0;i<tam;i++){
    lista2[i] = lista1[i];
  }
  
  return;
}

int comprobarLista(int *lista, int tam){
  int i;

  for(i = 1;i<tam; i++){
    if(lista[i-1] > lista[i]){
      return -1;
    }
  }

  return 0;
}

void *reservarMemoria(int tamano){

}

void swap(Lista lista, int *n1, int *n2){

}

int getElemento(Lista lista, int n){

}