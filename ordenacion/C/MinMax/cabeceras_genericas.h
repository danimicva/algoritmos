#ifndef _CABECERAS_GENERICAS_H_
#define _CABECERAS_GENERICAS_H_

#include "types.h"
#include "minmax.h"

int obtenerLongitudTablero();
char *obtenerTableroInicial();
int obtenerValorNodo(Nodo *nodo);
void generarHijos(Nodo *padre, int nJugador);

#endif
