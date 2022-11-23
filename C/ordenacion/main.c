#include <stdio.h>
#include <time.h>
#include "lista.h"
#include "lista_utils.h"


int main(int argc, char **argv){

  Lista *l;
  int i;

  l = generarListaAleatoria(5, time(NULL));
  
  printf("Elemento 3: %d\n", getElemento(*l, 3));
  printf("Comprobación lista: %d\n", comprobarLista(*l));

  imprimeLista(*l);

  liberarLista(l);
}

