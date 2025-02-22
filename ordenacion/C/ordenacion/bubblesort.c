#include "bubblesort.h"

long bubbleSort(int *lista, int tam){

  int i, j;
  long comp = 0;
  
  for(i = tam; i >= 0; i--){
    for(j = 0; j < i-1; j++){
      comp++;
      if(getElemento(lista, j) > getElemento(lista, j+1)){
        swap(lista, j, j+1);
      }
    }
  }
  return comp;
}