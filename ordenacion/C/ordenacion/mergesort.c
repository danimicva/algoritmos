#include "mergesort.h"

int merge(int *lista, int *lista1, int tam1, int *lista2, int tam2, long *comp);
int mergeSortInterno(int *lista, int tam, long *comp);
int dividirLista(int *listaOrigen, int tamOrigen, int **lista1, int *tam1, int **lista2, int *tam2);

long mergeSort(int *lista, int tam){
  
  long comp = 0;

  if(mergeSortInterno(lista, tam, &comp)){
    printf("Error mergesort.\n");
    return -1;
  }
  
  return comp;
}


int mergeSortInterno(int *lista, int tam, long *comp){
  
  int tam1, tam2;
  int *lista1, *lista2;
  
  if(tam == 1){
    return 0;
  }

  if(dividirLista(lista, tam, &lista1, &tam1, &lista2, &tam2)){
    printf("Error dividiendo lista.\n");
    return -1;
  }
  
  if(mergeSortInterno(lista1, tam1, comp) || mergeSortInterno(lista2, tam2, comp)){
    printf("Error combinando alguna lista\n");
    return -1;
  }
  
  if(merge(lista, lista1, tam1, lista2, tam2, comp)){
    printf("Error en el merge.\n");
    return -1;
  }
  
  return 0;
}

int merge(int *lista, int *lista1, int tam1, int *lista2, int tam2, long *comp){
  int  i = 0, j = 0,  k = 0;
  int *temp;

  temp = (int*) malloc(sizeof(int) * (tam1+tam2));
  if(!temp){
    printf("Error reservando memoria en merge.\n");
    return -1;
  }


  while(i < tam1 || j < tam2){
    (*comp)++;
    if((j == tam2 || lista1[i] <= lista2[j]) && i < tam1){
      //lista[k++] = lista1[i++];
      temp[k++] = lista1[i++];
    }else{
      //lista[k++] = lista2[j++];
      temp[k++] = lista2[j++];
    }
  }

  for(int i = 0; i < tam1 + tam2; i++){
    lista[i] = temp[i];
  }
  free(temp);

  //free(lista1);
  //free(lista2);

  return 0;
}

int dividirLista(int *listaOrigen, int tamOrigen, int **lista1, int *tam1, int **lista2, int *tam2){
  
  *tam1 = tamOrigen/2;
  *tam2 = tamOrigen - *tam1;
  /*
  *lista1 = (int *) malloc(sizeof(int) * (*tam1));
  *lista2 = (int *) malloc(sizeof(int) * (*tam2));
  if(lista1 == NULL || lista2 == NULL){
    printf("Error reservando memoria\n");
    return -1;
  }
  
   for(i = 0;i < tamOrigen; i++){
    if(i<*tam1){
      (*lista1)[i] = listaOrigen[i];
    }else{
      (*lista2)[i - *tam1] = listaOrigen[i]; 
    }
  }*/
  *lista1 = listaOrigen;
  *lista2 = &listaOrigen[*tam1];
  
  return 0;
}
