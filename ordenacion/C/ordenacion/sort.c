#include "sort.h"

int ejecutaAlgoritmos(int tamanoLista, Ejecucion *ejs);
int ejecutaMergeSort(int *lista, int tam, Ejecucion *ejecucion);
int ejecutaBubbleSort(int *lista, int tam, Ejecucion *ejecucion);
int ejecutaInsertionSort(int *lista, int tam, Ejecucion *ejecucion);

Ejecucion *ejecutaAlgoritmoMucho(int tamInicial, int intervalo, int nEjecuciones){

  Ejecucion *ejs;

  ejs = (Ejecucion *) malloc(sizeof(Ejecucion) * N_ALGORITMOS * nEjecuciones);
  if(ejs == NULL){
    printf("Error reservando memoria para las ejecuciones.\n");
    return NULL;
  }
 
  for(int i = 0, tam = tamInicial, nEj = 0; i < nEjecuciones; i ++, tam += intervalo, nEj += N_ALGORITMOS){
    if(ejecutaAlgoritmos(tam, &ejs[nEj])){
      printf("Error ejecutando algoritmos para tamaño: %d\n", i);
      return NULL;
    }
  }

  return ejs;

}

int ejecutaAlgoritmos(int tamanoLista, Ejecucion *ejs){

  int *listaOrig;
  int *listaCopia;
  

  listaOrig = generaLista(tamanoLista);
  listaCopia = generaLista(tamanoLista);
  if(listaOrig == NULL || listaCopia == NULL){
    printf("Error generando las listas.\n");
    return -1;
  }

  copiaLista(listaOrig, listaCopia, tamanoLista);
  if(ejecutaMergeSort(listaCopia, tamanoLista, &ejs[0])){
    free(listaOrig);
    free(listaCopia);
    printf("Error ejecutando mergesort.\n");
    return -1;
  }

  copiaLista(listaOrig, listaCopia, tamanoLista);
  if(ejecutaBubbleSort(listaCopia, tamanoLista, &ejs[1])){
    free(listaOrig);
    free(listaCopia);
    printf("Error ejecutando bubblesort.\n");
    return -1;
  }
  

  copiaLista(listaOrig, listaCopia, tamanoLista);
  if(ejecutaInsertionSort(listaCopia, tamanoLista, &ejs[2])){
    free(listaOrig);
    free(listaCopia);
    printf("Error ejecutando bubblesort.\n");
    return -1;
  }
  free(listaOrig);
  free(listaCopia);

  return 0;
}

int ejecutaMergeSort(int *lista, int tam, Ejecucion *ejecucion){

  struct timespec tstart={0,0}, tend={0,0};
  long comparaciones;

  clock_gettime(CLOCK_MONOTONIC, &tstart);
  comparaciones = mergeSort(lista, tam);
  clock_gettime(CLOCK_MONOTONIC, &tend);

  if(comparaciones == -1){
    printf("Error mergesort.\n");
    return -1;
  }

  ejecucion->algoritmo = "Merge sort";
  ejecucion->tamanoLista = tam;
  ejecucion->comparaciones = comparaciones;
  ejecucion->tiempo = (tend.tv_sec * 1000000000 + tend.tv_nsec) - (tstart.tv_sec * 1000000000 + tstart.tv_nsec);
  ejecucion->correcto = comprobarLista(lista, tam);
  return 0;
}

int ejecutaBubbleSort(int *lista, int tam, Ejecucion *ejecucion){;

  struct timespec tstart={0,0}, tend={0,0};
  long comparaciones;

  clock_gettime(CLOCK_MONOTONIC, &tstart);
  comparaciones = bubbleSort(lista, tam);
  clock_gettime(CLOCK_MONOTONIC, &tend);

  if(comparaciones == -1){
    printf("Error bubblesort.\n");
    return -1;
  }

  ejecucion->algoritmo = "Bubble sort";
  ejecucion->tamanoLista = tam;
  ejecucion->comparaciones = comparaciones;
  ejecucion->tiempo = (tend.tv_sec * 1000000000 + tend.tv_nsec) - (tstart.tv_sec * 1000000000 + tstart.tv_nsec);
  ejecucion->correcto = comprobarLista(lista, tam);
  return 0;

}

int ejecutaInsertionSort(int *lista, int tam, Ejecucion *ejecucion){;

  struct timespec tstart={0,0}, tend={0,0};
  long comparaciones;

  clock_gettime(CLOCK_MONOTONIC, &tstart);
  comparaciones = insertionSort(lista, tam);
  clock_gettime(CLOCK_MONOTONIC, &tend);

  if(comparaciones == -1){
    printf("Error insertion.\n");
    return -1;
  }

  ejecucion->algoritmo = "Insertion sort";
  ejecucion->tamanoLista = tam;
  ejecucion->comparaciones = comparaciones;
  ejecucion->tiempo = (tend.tv_sec * 1000000000 + tend.tv_nsec) - (tstart.tv_sec * 1000000000 + tstart.tv_nsec);
  ejecucion->correcto = comprobarLista(lista, tam);
  return 0;

}


