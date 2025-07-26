import logging
import random
from typing import List
import argparse

from gestor_ejecuciones import EjecucionPartidas
from resolvedores import (ResolvedorAleatorio, 
                          ResolvedorBase, 
                          ResolvedorFuerzaBruta, 
                          ResolvedorFuerzaBrutaMejorado, ResolvedorInteligente2Mejorado, 
                          ResolvedorPermutaciones, 
                          ResolvedorPermutacionesMejorado,
                          ResolvedorInteligente1,
                          ResolvedorInteligente1Mejorado)


def generar_objetivos_aleatorio(n_objetivos, caracteres, dificultad):
    ret = []
    for _ in range(n_objetivos):
        ret.append(''.join([caracteres[random.randint(0, len(caracteres)-1)] for _ in range(dificultad)]))
    
    return ret

def generar_todos_objetivos(caracteres, dificultad):
    
    cifras = dificultad
    base = len(caracteres)

    if base == 1:
        return caracteres[0]*cifras
    
    ret = []
    for i in range(pow(base, cifras)):

        intento = []

        valor = i

        for _ in range(cifras):
            intento.append(caracteres[valor % base])
            valor = valor // base

        ret.append(''.join(intento))
    
    return ret


parser = argparse.ArgumentParser()
parser.add_argument("caracteres", help="Los caracteres que están en juego, sin repetir.", type=str)
parser.add_argument("dificultad", help="El número de caracteres que tendrá la solución.", type=int)
parser.add_argument("max_intentos", help="Número máximo de intentos para resolver", type=int)
parser.add_argument("n_partidas", help="El número partidas que se harán.", type=int)
parser.add_argument("--salida", help="Fichero donde guardar la salida detallada de ejecución", required=False)
args = parser.parse_args()

logger = None

if args.salida:
    logger = logging.getLogger(name="mastermind")
    logging.basicConfig(filename=args.salida, encoding="utf-8", level=logging.INFO, filemode="w")
    
    
resolvedores: List[ResolvedorBase] = [
    # ResolvedorAleatorio,
    # ResolvedorFuerzaBruta,
    # ResolvedorFuerzaBrutaMejorado,
    # ResolvedorPermutaciones,
    # ResolvedorPermutacionesMejorado,
    ResolvedorInteligente1,
    ResolvedorInteligente1Mejorado,
    # ResolvedorInteligente2Mejorado
    ]

objetivos = []
if args.n_partidas == -1:
    objetivos = generar_todos_objetivos(args.caracteres, args.dificultad)
else:
    
    objetivos = generar_objetivos_aleatorio(args.n_partidas, args.caracteres, args.dificultad)

ejecucion = EjecucionPartidas(objetivos, args.caracteres, resolvedores, args.max_intentos, logger=logger)

ejecucion.ejecutar_partidas()

print(f"Número de partidas: {len(objetivos)}")
print()

ejecucion.imprimir_info_estadistica()
