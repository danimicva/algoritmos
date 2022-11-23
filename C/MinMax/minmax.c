#include "minmax.h"


static int nNodos = 0;
Nodo *crearNodo(char *tablero){
        Nodo *n = (Nodo*) malloc(sizeof(Nodo));
        if(!n){
                printf("Error reservando nodo.\n");
                return NULL;
        }
	n->tablero = (char*) malloc(obtenerLongitudTablero() * sizeof(char));
	if(!n->tablero){
		printf("Error reservando el tablero.\n");
		free(n);
		return NULL;
	}
        strncpy(n->tablero, tablero, obtenerLongitudTablero());
        n->nHijos = 0;
        n->hijos = (Nodo **) malloc(sizeof(Nodo *) * MAX_HIJOS);
        if(!n->hijos){
                printf("Error reservando array hijos.\n");
		free(n->tablero);
                free(n);
                return NULL;
        }
	
	nNodos++;

        return n;
}

int minMax(Nodo *nodo, int profundidad, int nJugador){

        int valor, valorHijo;

        valor = obtenerValorNodo(nodo);
//      printf("Prof: %d. Valor para {%s}: %d\n", profundidad, nodo->tablero, valor);
        // Si hemos llegado al fondo o si es estado -1 (empate), -2 (perdido) o 1 (ganado)
        if(profundidad == 0 || valor == -1 || valor == -2 || valor == 1)
                return valor;

        generarHijos(nodo, nJugador);
        if(nJugador == 0){
                valor = -INFINITO;
                for(int i = 0; i < nodo->nHijos; i++){
                        valorHijo = minMax(nodo->hijos[i], profundidad - 1, 1);
                        if(valorHijo > valor)
                                valor = valorHijo;
                }
        }else{
                valor = INFINITO;
                for(int i = 0; i < nodo->nHijos; i++){
                        valorHijo = minMax(nodo->hijos[i], profundidad - 1, 0);
                        if(valorHijo < valor)
                                valor = valorHijo;
                }
        }

        return valor;
}

int empiezaMinMax(Nodo *nodo, int profundidad, int nJugador){
        int ret = minMax(nodo, profundidad, nJugador);
        printf("Nodos totales: %d\n", nNodos);
	return ret;
}

void liberarNodos(Nodo *nodo){
        for(int i = 0; i < nodo->nHijos; i++)
                liberarNodos(nodo->hijos[i]);

	free(nodo->tablero);
        free(nodo->hijos);
        free(nodo);
}
