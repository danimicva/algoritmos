#ifndef _MINMAX_H_
#define _MINMAX_H_

#define INFINITO 9999999
#define MAX_HIJOS 10

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#include "types.h"
#include "cabeceras_genericas.h"

Nodo *crearNodo(char *tablero);

int empiezaMinMax(Nodo *nodo, int profundidad, int nJugador); 

void liberarNodos(Nodo *nodo);


#endif
