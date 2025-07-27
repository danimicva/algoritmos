import logging
import random
from typing import List
import argparse

from core import Mastermind
from gestor_ejecuciones import EjecucionPartidas
from resolvedores import (ResolvedorAleatorio, 
                          ResolvedorBase, 
                          ResolvedorFuerzaBruta, 
                          ResolvedorFuerzaBrutaMejorado, 
                          ResolvedorPermutaciones, 
                          ResolvedorPermutacionesMejorado,
                          ResolvedorInteligente)




parser = argparse.ArgumentParser()
parser.add_argument("caracteres", help="Los caracteres que están en juego, sin repetir.", type=str)
parser.add_argument("dificultad", help="El número de caracteres que tendrá la solución.", type=int)
parser.add_argument("max_intentos", help="Número máximo de intentos para resolver", type=int)
parser.add_argument("n_partidas", help="El número partidas que se harán.", type=int)
parser.add_argument("--salida", help="Fichero donde guardar la salida detallada de ejecución", required=False)
parser.add_argument("--partida", help="Partida concreta a resolver", type=str, required=False)
parser.add_argument("-i", "--interactivo", help="Modo interactivo.", action='store_true')
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
    ResolvedorInteligente,
    ]

objetivos = []
if args.partida:
    objetivos = [args.partida]
elif args.n_partidas == -1:
    objetivos = Mastermind.generar_todos_objetivos(args.caracteres, args.dificultad)
else:
    objetivos = Mastermind.generar_objetivos_aleatorio(args.n_partidas, args.caracteres, args.dificultad)

ejecucion = EjecucionPartidas(objetivos, args.caracteres, resolvedores, args.max_intentos, logger=logger)

ejecucion.ejecutar_partidas(args.interactivo)

print(f"Número de partidas: {len(objetivos)}")
print()

ejecucion.imprimir_info_estadistica()
