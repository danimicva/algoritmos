#include <stdio.h>
#include <string.h>
#include "sort.h"

void procesaEjecuciones(Ejecucion *ejecuciones, int nEjecuciones);

int main(int argc, char **argv){

  int tamInicial, tamFinal, intervalo, nEjecuciones;
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

  if(tamFinal < tamInicial){
    printf("El tamaño final no puede ser menor al inicial.\n");
    return -1;
  }else if(tamInicial == tamFinal || tamFinal - tamInicial < intervalo){
    nEjecuciones = 1;
  }else{
    nEjecuciones = (tamFinal - tamInicial) / intervalo;
  }

  ejecuciones = ejecutaAlgoritmoMucho(tamInicial, intervalo, nEjecuciones);
  if(ejecuciones == NULL){
    printf("Error ejecutando algoritmos\n");
    return -1;
  }

  procesaEjecuciones(ejecuciones, nEjecuciones);

  free(ejecuciones);
  
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

  fprintf(f,"Ejecución;Algoritmo;Elementos;tiempo;Comparaciones;\n");
  printf("%5s%15s%10s%13s%15s%10s\n","Ej","Algoritmo","Elementos","Tiempo","Comparaciones", "Correcto");

  for(i = 0; i < nEjecuciones * N_ALGORITMOS ; i++){
    fprintf(f,"%d;%s;%d;%ld;%ld;%s;\n", i, ejecuciones[i].algoritmo, ejecuciones[i].tamanoLista, ejecuciones[i].tiempo, ejecuciones[i].comparaciones, ejecuciones[i].correcto?"ERROR":"OK");
    printf("%5d%15s%10d%10ld ns%15ld%10s\n", i, ejecuciones[i].algoritmo, ejecuciones[i].tamanoLista, ejecuciones[i].tiempo, ejecuciones[i].comparaciones, ejecuciones[i].correcto?"ERROR":"OK");
  }

  fclose(f);

  return;
}
