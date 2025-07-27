
from abc import ABC, abstractmethod
from logging import Logger
import random
from typing import List

from core import Estado, Mastermind, MaxIntentosException


class ResolvedorBase(ABC):

    def __init__(self, partida: Mastermind, logger=None):
        self._partida: Mastermind = partida
        self._logger: Logger = logger
        
    def resolver(self):
        try:
            self._resolver_partida()
        except MaxIntentosException:
            # print(f"Partida no resuelta: {type(self).__name__}-{self._partida._objetivo}")
            pass
        except Exception as ex:
            print(f"Excepción en partida: {self._partida._objetivo}")
            raise ex from ex
    
    @abstractmethod
    def _resolver_partida(self):
        pass
    
    def _realizar_intento(self, intento, fase=None):
        return self._partida.realizar_intento(intento, fase)


class ResolvedorAleatorio(ResolvedorBase):

    def _resolver_partida(self):
        
        while self._partida.estado != Estado.FIN:
            
            intento = ''.join([self._partida.caracteres[random.randint(0, len(self._partida.caracteres)-1)] for _ in range(self._partida.dificultad)])
            
            self._realizar_intento(intento, "Aleatoria")
        
    
class ResolvedorFuerzaBruta(ResolvedorBase):
    """Resolvedor que prueba todas las combinaciones posibles con los caracteres disponibles."""

    def _resolver_partida(self):

        cifras = self._partida.dificultad
        base = len(self._partida.caracteres)

        if base == 1:
            self._realizar_intento(self._partida.caracteres[0]*self._partida.dificultad, "Fuerza bruta")
            return
        
        for i in range(pow(base, cifras)):

            intento = []

            valor = i

            for _ in range(cifras):
                intento.append(self._partida.caracteres[valor % base])
                valor = valor // base

            self._realizar_intento(''.join(intento), "Fuerza bruta")

            if self._partida.estado == Estado.FIN:
                return


class ResolvedorFuerzaBrutaMejorado(ResolvedorBase):
    """Resolvedor que prueba todas las combinaciones posibles con sólo los caracteres que están en la solución."""

    def _resolver_partida(self):

        # Resuelve igual que el fuerza bruta, pero primero mira los caracteres realmente 
        # presentes para no probar combinaciones no existentes.

        caracteres_reales = ""
        for c in self._partida.caracteres:
            self._realizar_intento(c*self._partida.dificultad, "Búsqueda caracteres")
            if(self._partida.intentos[-1].buena_posicion > 0):
                caracteres_reales += c
        
        cifras = self._partida.dificultad
        base = len(caracteres_reales)

        if base == 1:
            self._realizar_intento(caracteres_reales[0]*self._partida.dificultad, "Fuerza bruta")
            return
        
        for i in range(pow(base, cifras)):

            intento = []

            valor = i

            for _ in range(cifras):
                intento.append(caracteres_reales[valor % base])
                valor = valor // base

            self._realizar_intento(''.join(intento), "Fuerza bruta")

            if self._partida.estado == Estado.FIN:
                return


class ResolvedorPermutaciones(ResolvedorBase):
    """Resolvedor que:
      1. Obtiene los distintos valores disponibles.
      2. Calcula todas las permutaciones posibles."""
    def _resolver_partida(self):

        caracteres_solucion = self._obtener_caracteres_solucion()
        
        self._probar_solucion_recursivo([], caracteres_solucion)
    
    def _obtener_caracteres_solucion(self):
        caracteres_solucion = []
        for c in self._partida.caracteres:
            self._realizar_intento(c*self._partida.dificultad, "Obtener caracteres")
            for _ in range(self._partida.intentos[-1].buena_posicion):
                caracteres_solucion.append(c)
                
        return caracteres_solucion
        
    
    def _probar_solucion_recursivo(self, base, resto):
        
        if len(resto) == 0:
            self._realizar_intento(''.join(base), "Permutaciones")
            return self._partida.estado == Estado.FIN
        
        for i in range(len(resto)):
            r = resto[:]
            r.remove(resto[i])
            if self._probar_solucion_recursivo([*base, resto[i]], r):
                return True
        
        
class ResolvedorPermutacionesMejorado(ResolvedorPermutaciones):
    """Resolvedor que:
      1. Obtiene los distintos valores disponibles.
      2. Calcula todas las permutaciones posibles."""

    def _obtener_caracteres_solucion(self):
        caracteres_solucion = []
        n_caracteres_solucion = 0
        for c in self._partida.caracteres:
            self._realizar_intento(c*self._partida.dificultad, "Obtener caracteres")
            for _ in range(self._partida.intentos[-1].buena_posicion):
                caracteres_solucion.append(c)
                n_caracteres_solucion += 1
            if n_caracteres_solucion == self._partida.dificultad:
                break
        
        return caracteres_solucion
        

class ResolvedorInteligente(ResolvedorBase):
    """Resolvedor que:
      1. Obtiene los distintos valores de la solución y un caracter que no esté presente.
      2. Va buscando dónde va cada caracter.
      OJO Requiere que haya más caracteres que dificultad, si no no funciona."""
    
    # Nivel 3 de mejora: Inducir casos que no sea necesario probar. Por ejemplo, si estoy buscando caracteres y me queda sólo uno por mirar, 
    # no es necesario mirarlo, por descarte tiene que ser. Aplicarlo en:
    #  -
    #  - (Hecho) Al revisar los posibles caracteres de más, si solo queda uno en la lista, debe ser ese 
    #  - Al buscar la solución, si solo queda un caracter posible, ese debe rellenar los huecos
    def __init__(self, partida: Mastermind, logger=None):
        super().__init__(partida, logger)
        
        if len(partida.caracteres) <= partida.dificultad:
            raise Exception("Este resolvedor requiere que haya más caracteres que dificultad, porque requiere un caracter vacío")
        
        self.solucion_final: List[int] = []
        self.caracteres_posibles = []
        self.parejas_posibles = []
        self.caracter_no_presente = None


    def _resolver_partida(self):
        # self._encontrar_caracteres_presentes_unoauno()
        self._encontrar_caracteres_presentes_dosendos()

        self._encontrar_posicion_caracteres()

        # En este punto ya deberíamos tener la solución final totalmente construida, así que la realizamos.
        self._realizar_intento(''.join(self.solucion_final), "Resolver")

    def _encontrar_caracteres_presentes_unoauno(self):
        # Obtenemos los caracteres de la solución y su cantidad
        
        n_caracteres_solucion = 0
        for c in self._partida.caracteres:
            self._realizar_intento(c*self._partida.dificultad, "Encontrar caracteres")
            disponibles = self._partida.intentos[-1].buena_posicion + self._partida.intentos[-1].mala_posicion
            if disponibles > 0:
                self.caracteres_posibles.append([c, disponibles])
            else:
                self.caracter_no_presente = c
            n_caracteres_solucion += self._partida.intentos[-1].buena_posicion
            if n_caracteres_solucion == self._partida.dificultad:
                break
            
        # Si no se ha encontrado un no presente, es que los presentes han sido los primeros en salir, así que el último no estará nunca.
        if not self.caracter_no_presente:
            self.caracter_no_presente = self._partida.caracteres[-1]


    def _encontrar_caracteres_presentes_dosendos(self):

        self._obtener_parejas_candidatos()

        self._obtener_caracteres_presentes_de_parejas()

        # Si no se ha encontrado un no presente, es que los presentes han sido los primeros en salir, así que el último no estará nunca.
        if not self.caracter_no_presente:
            self.caracter_no_presente = self._partida.caracteres[-1]


    def _obtener_parejas_candidatos(self):
        # Mejora: En la última pareja, mirar sólo el primero.
        
        n_caracteres_solucion = 0

        # Primero buscamos los caracteres por parejas para ahorrarnos búsquedas.
        # El -1 es para evitar la búsqueda de la última pareja y buscarla toda del tirón
        # TODO mejorar para dificultad N y número de caracteres impar
        for i in range(len(self._partida.caracteres) // 2):
            c1 = self._partida.caracteres[2*i]
            c2 = self._partida.caracteres[2*i + 1]
            intento = c1*3 + c2*2
            buenos, malos = self._realizar_intento(intento, "Encontrar caracteres")
            
            if buenos + malos > 0:
                self.parejas_posibles.append([c1, c2, buenos + malos])
            else:
                self.caracter_no_presente = c1
            n_caracteres_solucion += buenos + malos
            if n_caracteres_solucion == self._partida.dificultad:
                break
        
        # # Si no los hemos encontrado aún, buscamos con el primer valor de la última pareja
        # if n_caracteres_solucion != self._partida.dificultad:
        #     intento = self._partida.caracteres[-2]*5
        #     buenos, _ = self._realizar_intento(intento, "Encontrar caracteres")
        #     # Si no devuelve ninguno, todos son del segundo
        #     if buenos == 0:

        #     else:
                
        
    def _obtener_caracteres_presentes_de_parejas(self):
        
        candidatos_con_quiza_mas = []
        # Ahora tenemos los caracteres, por parejas, que pueden estar o no
        # Vamos probando por cada uno para sacar cuántos hay.
        for cp in self.parejas_posibles:
            intento = cp[0] * self._partida.dificultad
            buenos, _ = self._realizar_intento(intento, "Encontrar caracteres")
            # si no hay, es que todos eran del segundo
            if buenos == 0:
                self.caracteres_posibles.append([cp[1], cp[2]])
                if not self.caracter_no_presente:
                    self.caracter_no_presente = cp[0]
            # si hay los mismos que vimos antes, es que todso eran del 1
            elif buenos == cp[2]:
                self.caracteres_posibles.append([cp[0], cp[2]])
                if not self.caracter_no_presente and cp[2] < 3:
                    self.caracter_no_presente = cp[1]
            # Si no, es que hay mezcla:
            else: #(me tengo que ir, añadir con c1 disponible veces y c2 disponible menos cp[2] veces)
                self.caracteres_posibles.append([cp[0], buenos])
                if buenos < cp[2]:
                    self.caracteres_posibles.append([cp[1], cp[2] - buenos])
            
            # Si se han obtenido 3 o más con el primer caracter puede que haya algunos del segundo caracter ocultos (caso SAAAA)
            if buenos >= 3:
                candidatos_con_quiza_mas.append([cp[1], 0])
            # Si se han obtenido 0 con el primer caracter y había 2 o más resultados, puede que haya más resultados del segundo ocultos
            elif cp[2] - buenos >= 2: 
                candidatos_con_quiza_mas.append([cp[1], cp[2] - buenos])

        # Para el caso que no hayamos encontrado todos, temeos que revisar los que quizá tengan más
        if sum(cs[1] for cs in self.caracteres_posibles) < self._partida.dificultad:
                for i in range(len(candidatos_con_quiza_mas)):
                    if i == len(candidatos_con_quiza_mas) - 1:
                        self._aplicar_nuevo_caracter(
                            candidatos_con_quiza_mas[i][0], 
                            self._partida.dificultad - sum(cs[1] for cs in self.caracteres_posibles if cs[0] != candidatos_con_quiza_mas[i][0]))
                        break

                    cqm = candidatos_con_quiza_mas[i]

                    intento = cqm[0] * self._partida.dificultad
                    buenos, _ = self._realizar_intento(intento, "Encontrar caracteres")
                    
                    # Si volviendo a consultar obtenemos más que antes, tenemos que incluir o sobreescribir el valor y ver si ya tenemos todo.
                    if buenos > cqm[1]:
                        self._aplicar_nuevo_caracter(cqm[0], buenos)

                        if sum(cs[1] for cs in self.caracteres_posibles) == self._partida.dificultad:
                            break

    def _aplicar_nuevo_caracter(self, caracter, cantidad):
        if not any(cs[0] == caracter for cs in self.caracteres_posibles):
            self.caracteres_posibles.append([caracter, cantidad])
        else:
            for cs in self.caracteres_posibles:
                if cs[0] == caracter:
                    cs[1] = cantidad
                    break

    def _encontrar_posicion_caracteres(self):
        self.solucion_final = [None] * self._partida.dificultad
        # Ahora iremos uno por uno buscando su posición.
        for caracter_cantidad in self.caracteres_posibles:
            posiciones = self._encontrar_posiciones_caracter(caracter_cantidad[0], caracter_cantidad[1])

            # En este punto hemos encontrado la posición buena de los caracteres, así que los ponemos en la solución final
            for p in posiciones:
                self.solucion_final[p] = caracter_cantidad[0]


    def _encontrar_posiciones_caracter(self, caracter, cantidad):
        # Para probar dónde estará cada caracter, vamos a usar un array con las posiciones de cada uno de ellos. 
        # Empezaremos colocándolos en las primeras posiciones (0, 1...), según cuántos haya.
        posiciones = self._iniciar_posiciones_caracter(cantidad)

        # El primer intento lo hacemos directamente porque todavía no hemos iterado resultados
        intento = self._generar_intento_de_posiciones(caracter, posiciones)
        self._realizar_intento(intento, "Encontrar posiciones")
        acertados = self._partida.intentos[-1].buena_posicion
        
        while(acertados < cantidad):
            # Mientras no encontremos todas las posiciones, vamos avanzando el último valor. 
            posiciones[-1] += 1
            
            posiciones = self._revisar_posiciones(posiciones)
            
            intento = self._generar_intento_de_posiciones(caracter, posiciones)
            self._realizar_intento(intento, "Encontrar posiciones")
            acertados = self._partida.intentos[-1].buena_posicion
        
        return posiciones

    def _iniciar_posiciones_caracter(self, cantidad):
        # Para probar dónde estará cada caracter, vamos a usar un array con las posiciones de cada uno de ellos. 
        # Empezaremos colocándolos en las primeras posiciones (0, 1...), según cuántos haya.
        # posiciones = []
        # for i in range(cantidad):
        #     posiciones.append(i)
            
        # return posiciones
    
        # Mejora: Si la posicion a buscar está en la solución final, nos la saltamos.
        posiciones = []
        i = 0
        while len(posiciones) < cantidad:
            # Mejora: Si la posicion a buscar está en la solución final, nos la saltamos.
            if self.solucion_final[i] is None:
                posiciones.append(i)
            i += 1
            
        return posiciones

    def _revisar_posiciones(self, posiciones):

        # Mejora: evitamos también posiciones ya descubiertas. Para ello, si al aumentar está ya en solución, aumentamos otra
        while posiciones[-1] < self._partida.dificultad and self.solucion_final[posiciones[-1]] is not None:
            posiciones[-1] += 1
        
        # Comprobamos desde atrás el array, mirando que los valores son correctos
        for i in range(1, len(posiciones)+1):
            # Si la posición a mirar es superior al valor máximo que puede obtener (la última la dificultad, la penúltima la dificultad menos 1, etc.)
            # Aumentamos de valor la posición anterior y actualizamos el resto de la cadena a los valores consecutivos.
            # En la siguiente vuelta comprobaremos esta posición anterior para ver si es viable, Si no, repetiremos lo mismo.
            # Si sólo hay una posición, antes de que este if devuelva true lo habremos encontrado (habríamos pasado por todas las posiciones sin encontrarlo)
            if posiciones[-i] >= self._partida.dificultad - (i - 1):
                posiciones[-(i+1)] += 1
                # Tras ello, avanzamos el resto de posiciones al valor consecutivo
                for j in range(i):
                    posiciones[-(i-j)] = posiciones[-(i-j+1)] + 1
            else:
                # Si la posición actual no supera el valor máximo, salimos de este bucle para volver a intentarlo
                return posiciones

    def _generar_intento_de_posiciones(self, caracter_buscado, posiciones):
        """Esta función genera un intento a partir de una lista de posiciones donde colocar un caracter buscado 
           y rellenando el resto con el caracter no presente."""
        r = []
        for i in range(self._partida.dificultad):
            if i in posiciones:
                r.append(caracter_buscado)
            else:
                r.append(self.caracter_no_presente)

        return ''.join(r)





