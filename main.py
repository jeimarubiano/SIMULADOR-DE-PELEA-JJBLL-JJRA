from juego import *
while salud_heroe > 0 and salud_enemigo >  0:
    mostrar_estado()
    turno_jugador()
    if verificar_ganador():
        break
    turno_enemigo()
    if verificar_ganador():
        break