from random import randint


"""Piedra = 1,
    Papel = 2,
    Tijera = 3"""

puntos_jugador = 0
puntos_maquina = 0

jugar = True
while jugar:  # if jugar == True

    option = """\n Elige una opción:\n 
    1. Piedra.
    2. Papel.
    3. Tijera: """

    respuesta = int(input(option))

    maquina = randint(1, 3)

    if respuesta == 1:
        if maquina == 1:
            print("\n Empate")

        elif maquina == 2:
            print("\n Papel envuelve a piedra. Pierdes")
            puntos_maquina = puntos_maquina + 1

        elif maquina == 3:
            print("\n Piedra machaca tijera. Tu ganas")
            puntos_jugador = puntos_jugador + 1

    elif respuesta == 2:
        if maquina == 1:
            print("\n Papel envuelve a piedra. Tu ganas")
            puntos_jugador = puntos_jugador + 1

        elif maquina == 2:
            print("\n Empate")

        elif maquina == 3:
            print("\n Tijeras cortan papel. Tu ganas")
            puntos_maquina = puntos_maquina + 1

    elif respuesta == 3:
        if maquina == 1:
            print("\n Piedra machaca tijera. Pierdes")
            puntos_maquina = puntos_maquina + 1

        elif maquina == 2:
            print("\n Tijeras cortan papel. Tu ganas")
            puntos_jugador = puntos_jugador + 1

        elif maquina == 3:
            print("\n Empate")

    print(
        f"\n Puntuación: \n   Jugador:{puntos_jugador}\n   Máquina:{puntos_maquina}\n ")

    respuesta = input("¿Quieres seguir jugando? (Y/N): ").upper()
    if respuesta == "Y":
        jugar = True
    else:
        jugar = False
