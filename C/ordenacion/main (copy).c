#include <stdio.h>
#include <string.h>
#include "sort.h"

void procesaEjecuciones(Ejecucion *ejecuciones, int nEjecuciones);

int main(int argc, char **argv){

  int tamInicial, tamFinal, intervalo;
  Ejecucion *ejecuciones;

  if(argc != 4){
    printf("Error en los argumentos: ./sort <tamanoListaInicial> <tamanolistaFinal> <intervalo>\n");
    return -1;
  }

  tamInicial = atoi(argv[1]);
  tamFinal = atoi(argv[2]);
  intervalo = atoi(argv[3]);
  if(tamInicial == 0 || tamFinal == 0 || intervalo == 0){
    printf("Por favor, introduzca un números naturales.\n");
    return -1;
  }
 
  if(tamFinal < tamInicial){
    printf("Error. Tamaño final mayor que el inicial.\n");
    return -1;
  }

  ejecuciones = ejecutaAlgoritmoMucho(tamInicial, tamFinal, intervalo);
  if(ejecuciones == NULL){
    printf("Error ejecutando algoritmos\n");
    return -1;
  }

  procesaEjecuciones(ejecuciones, (((tamFinal - tamInicial)/intervalo) * N_ALGORITMOS) + N_ALGORITMOS);

  return 0;

}

void procesaEjecuciones(Ejecucion *ejecuciones, int nEjecuciones){

  FILE *f;
  int i;

  f = fopen("salida.csv", "w");
  if(!f){
    printf("Error abriendo fichero de salida.\n");
    return;
  }

  fprintf(f,"Ejecucion;Algoritmo;Elementos;tiempo;Comparaciones;\n");
//  printf("Ejecucion\tAlgoritmo\tElementos\tTiempo\tComparaciones\t\n");

  for(i = 0; i < nEjecuciones ; i++){
    fprintf(f,"%d;%s;%d;%ld;%ld;%s;\n", i, ejecuciones[i].algoritmo, ejecuciones[i].tamanoLista, ejecuciones[i].tiempo, ejecuciones[i].comparaciones, ejecuciones[i].correcto?"ERROR":"OK");
  }

  fclose(f);

  return;
}
