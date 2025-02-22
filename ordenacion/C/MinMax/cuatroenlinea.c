#include "cabeceras_genericas.h"

int obtenerLongitudTablero(){
	return 12;
}

char *obtenerTableroInicial(){
	char *ret = malloc(sizeof(char) * obtenerLongitudTablero());
	if(!ret){
		printf("Error reservando memoria para el tablero inicial.\n");
		return NULL;
	}

	// 42 espacios
//	strncpy(ret, "                                          ", 42);
//	12 espacios
	strncpy(ret, "            ", 12);

	return ret;
}

// 1 victoria, 0 sin terminar, -1 empate, -2 derrota
int obtenerValorNodo(Nodo *nodo){
	// Primero miramos victorias en horizontal (las celdas 18-24 son la fila del medio
/*
	for(int i = 18; i < 24; i++){
		// Si la casilla central está vacía no puede hacer 4 en raya
		if(nodo->tablero[i] == ' ')
			continue;
		int n = 0;
		for(int j = -3; j < 4; j++){
			if(nodo->tablero[i] == nodo->tablero[i+j*6])
				n++;
			else
				n = 0;
			if(n == 4)
				return nodo->tablero[i] == 'X' ? 1 : -2;
		}
	}

	// Comprobamos las victorias verticales
	for(int i = 2; i <= 38; i+= 6){
		if(nodo->tablero[i] == ' ')
			continue;
		int n = 0; 
		for(int j = i - 2; j < i + 4; j++){
			if(nodo->tablero[i] == nodo->tablero[i + j])
				n++;
			else
				n = 0;
			if(n == 4)
				return nodo->tablero[i] == 'X' ? 1 : -2;
		}

	}
*/
	return 0;
}
void generarHijos(Nodo *padre, int nJugador){
        char tableroTemp[12];
	int filas = 3, columnas = 4;
//	printf("len: %d\n", strlen(padre->tablero));
        strncpy(tableroTemp, padre->tablero, obtenerLongitudTablero());
//	printf("Generando hijos para {%s}\n", tableroTemp);

        for(int i = 0; i < columnas; i++){
		for(int j = 0; j < filas; j++){
	                if(tableroTemp[i*filas+j] == ' '){
        	                tableroTemp[i*filas+j] = (nJugador == 0 ? 'X' : 'O');
                	        Nodo *hijo = crearNodo(tableroTemp);
                        	if(!hijo){
	                                printf("Error reservando nodo.\n");
        	                        return;
                	        }
//                      	printf("Generado hijo %d: {%s}\n", i, hijo->tablero);
	                        padre->hijos[padre->nHijos++] = hijo;
        	                tableroTemp[i*filas+j] = ' ';
				break;
                	}
		}
        }
//	printf("Hijos creados: %d\n", padre->nHijos);
}
