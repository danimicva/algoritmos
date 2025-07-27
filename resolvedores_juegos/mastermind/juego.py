import argparse
from core import Mastermind, Estado

parser = argparse.ArgumentParser()
parser.add_argument("caracteres", help="Los caracteres que están en juego, sin repetir.", type=str)
parser.add_argument("dificultad", help="El número de caracteres que tendrá la solución.", type=int)
parser.add_argument("max_intentos", help="Número máximo de intentos para resolver", type=int)
parser.add_argument("--partida", help="Partida concreta a resolver", type=str, required=False)
args = parser.parse_args()


print("¡Bienvenido al juego de Mastermind!")

print("Empieza la partida.")

objetivo = args.partida if args.partida else Mastermind.generar_objetivos_aleatorio(1, args.caracteres, args.dificultad)[0]

m = Mastermind(objetivo, args.caracteres, args.max_intentos)

while m.estado != Estado.FIN:
    m.imprimir_partida(False)
    print()
    intento = input("Introduce tu jugada: ")
    try:
        m.realizar_intento(intento)
    except Exception as ex:
        print(f"El valor introducido {intento} no es correcto: {str(ex)}")


m.imprimir_partida(True)
print("Bien, conseguiste ganar!")