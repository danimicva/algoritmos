#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#include "types.h"
#include "minmax.h"
#include "cabeceras_genericas.h"

void main(int argc, char* argv[]){

	char *tablero;
	int prof;

	if(argc != 2){
		printf("Error, hace falta un argumento de profundidad numérico.\n");
		return;
	}

	prof = atoi(argv[1]);
	if(prof <= 0){
		printf("Profundidad incorrecta: %s\n", argv[1]);
		return;
	}


	tablero = obtenerTableroInicial();
	Nodo *nodo = crearNodo(tablero);

	int valor = empiezaMinMax(nodo, prof, 0);

	free(tablero);
	liberarNodos(nodo);

	printf("Valor: %d\n", valor);

}
