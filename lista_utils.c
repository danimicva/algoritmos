#include "lista_utils.h"


Lista *generarListaAleatoria(int tamano, long seed){

  Lista *lista;
  int i;
  
  lista = crearLista(tamano);
  if(!lista){
    return NULL;
  }

  srand(seed);
  
  for(i = 0; i<tamano; i++){
    setElemento(*lista, i, rand() % tamano);
  }
  
  return lista;
}

int comprobarLista(Lista lista){
  int i;

  for(i = 1;i<getTamano(lista); i++){
    if(getElemento(lista, i-1) > getElemento(lista, i)){
      return -1;
    }
  }
  return 0;
}