from enum import Enum
from typing import List

class MaxIntentosException(Exception):
    pass

class Estado(Enum):
    JUGANDO = 1
    FIN = 2

class Intento:
    def __init__(self, valor, buena_posicion, mala_posicion, fase=None):
        self.valor = valor
        self.buena_posicion = buena_posicion
        self.mala_posicion = mala_posicion
        self.fase = fase

    def __str__(self):
        return self.valor + ": " + ('X' * self.buena_posicion) + ('O' * self.mala_posicion)
    

class Mastermind:
    
    def __init__(self, objetivo, caracteres, max_intentos):        
        self.dificultad = len(objetivo)
        self.caracteres = caracteres
        self._objetivo = objetivo
        self.intentos: List[Intento] = []
        self.estado = Estado.JUGANDO
        self.max_intentos = max_intentos

    def _evaluar_intento(self, intento):
        
        intento_evaluados = []
        objetivo_evaluados = []
        buena_posicion = 0
        mala_posicion = 0

        # Primero evaluamos los que están bien colocados, guardando todo lo que hemos mirado.
        for i in range(len(intento)):
            if intento[i] == self._objetivo[i]:
                intento_evaluados.append(i)
                objetivo_evaluados.append(i)
                buena_posicion += 1

        # Ahora evaluamos los que están en mala posición
        for i in range(len(intento)):
            if i in intento_evaluados:
                continue
            # Comparamos cada resultado con los demás que están disponibles
            for j in range(len(intento)):
                if j in objetivo_evaluados:
                    continue
                if intento[i] == self._objetivo[j]:
                    objetivo_evaluados.append(j)
                    intento_evaluados.append(i)
                    mala_posicion += 1
                    break

        return Intento(intento, buena_posicion, mala_posicion)


    def realizar_intento(self, intento, fase=None):
        if len(intento) != self.dificultad:
            raise Exception(f"El intento no cumple con la dificultad ({self.dificultad})")
        
        r = self._evaluar_intento(intento)
        if fase:
            r.fase = fase

        self.intentos.append(r)

        if(intento == self._objetivo):
            self.estado = Estado.FIN
        elif self.max_intentos > 0 and len(self.intentos) >= self.max_intentos:
            raise MaxIntentosException("Máximo número de intentos realizados")

        return self.intentos[-1].buena_posicion, self.intentos[-1].mala_posicion
        

    def imprimir_partida(self, mostrar_objetivo=False):
        print()
        print("------------------------")
        
        print("| Objetivo: " + (self._objetivo if mostrar_objetivo else '*' * self.dificultad))
        print("|")
        for i in range(len(self.intentos)):
            print(f"| {i + 1}: {self.intentos[i]}")
        print()
    