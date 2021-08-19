import random

while True:
    juegos = ["piedra", "papel", "tijeras"]
    maxPts = 0

    while maxPts == 0:
        try:
            maxPts = int(input("A los cuantos puntos se decidirá el ganador? "))
            if maxPts not in range(1, 6):
                print("Solamente se puede de 1 a 5")
                maxPts = 0
        except ValueError:
            print("Ingrese un número")
            maxPts = 0

    marcador = [0, 0]
    print("Empieza el juego!")
    while marcador[0] < maxPts and marcador[1] < maxPts:
        juegoJugador = input('\nQue quieres jugar?: ').lower()
        if juegoJugador not in juegos:
            print("Solamente puedes jugar piedra, papel o tijeras")
            continue
        juegoCPU = random.choice(juegos)

        print("La CPU jugó " + juegoCPU)
        if juegoJugador == juegoCPU:
            print('Empate!' + (
                " el marcador continua " + str(marcador[0]) + '-' + str(marcador[1]) if maxPts != 1 else ""))
            continue
        if (juegoJugador == 'piedra' and juegoCPU == 'tijeras') or (juegoJugador == 'papel' and juegoCPU == 'piedra') or (juegoJugador == 'tijeras' and juegoCPU == 'papel'):
            marcador[0] += 1
            print("Ganaste!" + (
                " el marcador va " + str(marcador[0]) + '-' + str(marcador[1]) if maxPts != 1 else ""))
            continue

        marcador[1] += 1
        print("Perdiste!" + (
            " el marcador va " + str(marcador[0]) + '-' + str(marcador[1]) if maxPts != 1 else ""))

    if marcador[0] > marcador[1]:
        print('\nGanaste el juego!')
    else:
        print('\nPerdiste el juego!')

    sigJuego = input('Quieres volver a jugar? (si/no): ').lower()
    if sigJuego != 'si':
        break
