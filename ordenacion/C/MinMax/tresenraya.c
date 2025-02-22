#include "cabeceras_genericas.h"

int obtenerLongitudTablero(){
	return 9;
}

char *obtenerTableroInicial(){
	char *ret = malloc(sizeof(char) * 9);
	if(!ret){
		printf("Error reservando memoria para el tablero inicial.\n");
		return NULL;
	}

	strncpy(ret, "         ", 9);

	return ret;
}

int obtenerValorNodo(Nodo *nodo){
        // Victoria/derrota pasando por el medio
        if(nodo->tablero[4] != ' ' && ((nodo->tablero[4] == nodo->tablero[0]
                        && nodo->tablero[4] == nodo->tablero[8]) ||
                        (nodo->tablero[4] == nodo->tablero[2]
                                && nodo->tablero[4] == nodo->tablero[6]) ||
                        (nodo->tablero[4] == nodo->tablero[1]
                                && nodo->tablero[4] == nodo->tablero[7]) ||
                        (nodo->tablero[4] == nodo->tablero[3]
                                && nodo->tablero[4] == nodo->tablero[5])))
                return nodo->tablero[4] == 'X' ? 1 : -2;

        // Victoria/derrota izquierda arriba
        if(nodo->tablero[0] != ' ' && ((nodo->tablero[3] == nodo->tablero[0]
                        && nodo->tablero[3] == nodo->tablero[6]) ||
                        (nodo->tablero[1] == nodo->tablero[0]
                                && nodo->tablero[1] == nodo->tablero[2])))
                return nodo->tablero[0] == 'X' ? 1 : -2;

        // Victoria/derrota derecha abajo
        if(nodo->tablero[8] != ' ' && ((nodo->tablero[5] == nodo->tablero[2]
                        && nodo->tablero[5] == nodo->tablero[8]) ||
                        (nodo->tablero[7] == nodo->tablero[6]
                                && nodo->tablero[7] == nodo->tablero[8])))
                return nodo->tablero[8] == 'X' ? 1 : -2;


        //Caso de empate
        if(nodo->tablero[0] != ' ' && nodo->tablero[1] != ' '
                        && nodo->tablero[2] != ' ' && nodo->tablero[3] != ' '
                        && nodo->tablero[4] != ' ' && nodo->tablero[5] != ' '
                        && nodo->tablero[6] != ' ' && nodo->tablero[7] != ' '
                        && nodo->tablero[8] != ' ')
                return -1;

        // Si todavía no ha terminado
        return 0;
}

void generarHijos(Nodo *padre, int nJugador){
        char tableroTemp[9];

        strncpy(tableroTemp, padre->tablero, 9);
//	printf("Generando hijos para {%s}\n", tableroTemp);

        for(int i = 0; i < 9; i++){
                if(tableroTemp[i] == ' '){
                        tableroTemp[i] = (nJugador == 0 ? 'X' : 'O');
                        Nodo *hijo = crearNodo(tableroTemp);
                        if(!hijo){
                                printf("Error reservando nodo.\n");
                                return;
                        }
//			printf("Generado hijo %d: {%s}\n", i, hijo->tablero);
                        padre->hijos[padre->nHijos++] = hijo;
                        tableroTemp[i] = ' ';
                }
        }
//	printf("Hijos creados: %d\n", padre->nHijos);
}
