def mostrar_posicion(x, y):
    print(f"Posición actual del robot: ({x}, {y})")

def mover_robot(comando, x, y):
    if comando == "arriba" and y < 4:
        y += 1
    elif comando == "abajo" and y > 0:
        y -= 1
    elif comando == "derecha" and x < 4:
        x += 1
    elif comando == "izquierda" and x > 0:
        x -= 1
    else:
        print("Movimiento inválido: el robot no puede salir de la cuadrícula.")
    return x, y

def main():
    x, y = 0, 0  # Posición inicial del robot
    print("Bienvenido al simulador de robot.")
    print("Instrucciones:")
    print(" - Usa 'arriba', 'abajo', 'izquierda' o 'derecha' para mover el robot.")
    print(" - Usa 'salir' para terminar el programa.")

    while True:
        mostrar_posicion(x, y)
        comando = input("Ingresa un comando: ").strip().lower()

        if comando == "salir":
            print("¡Gracias por usar el simulador de robot! ¡Hasta luego!")
            break
        elif comando in ["arriba", "abajo", "izquierda", "derecha"]:
            x, y = mover_robot(comando, x, y)
        else:
            print("Comando no válido. Intenta de nuevo.")

# Iniciar el programa
main()