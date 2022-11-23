#include "utils.h"

void *reservarMemoria(int tamano){
  return malloc(tamano);
}

void liberarMemoria(void *obj){
  return free(obj);
}
