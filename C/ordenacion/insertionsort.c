#include "insertionsort.h"

long insertionSort(int *lista, int tam){

  int i, j;
  long comp = 0;
  
  for(i = 1; i < tam; i++){
    j = i;
    while(j > 0 && lista[j-1] > lista[j]){
      comp++;
      swap(lista, j-1, j);
      j--;
    }
  }
  return comp;
}