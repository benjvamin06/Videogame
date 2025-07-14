jugador = {
    "Vida" : 100,
    "Ataque" : 100,
    "Defensa" : 100,
    "Experiencia": 100,
    "Inventario" : 10
}

def inicio():
    nombre = input("Ingrese su nombre jugador: ")
    print(f"¡ Bienvenido {nombre} !")
    print(f"Actualmente tus atributos {nombre} son los siguientes: {jugador}. Podrás ir mejorandolos a medida que vas avanzando. ")
    return


while True:
    print("Ecos del Abismo")
    print("1.- Iniciar Juego")

    opc = int(input("Ingrese una opción: "))
    if opc == 1:
        inicio()