#ifndef _TYPES_H_
#define _TYPES_H_

typedef struct Nodo{
        char *tablero;
        int nHijos;
        struct Nodo** hijos;
}Nodo;

#endif
