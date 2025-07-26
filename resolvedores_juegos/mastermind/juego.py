from core import Mastermind, Estado


print("¡Bienvenido al juego de Mastermind!")

print("Empieza la partida.")



m = Mastermind("ASDFGH", "ASDFGH")

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