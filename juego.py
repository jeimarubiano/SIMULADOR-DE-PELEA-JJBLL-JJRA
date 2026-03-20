import random
nombre_heroe = input("Ingresa nombre de heroe: ")
nombre_enemigo = input("Ingresa nombre de enemigo: ")
salud_heroe = 100
salud_enemigo_max = 120
salud_enemigo = salud_enemigo_max
pociones = 3
cura = random.randint(20, 20)
mostrar = ""
def generar_daño():
    daño = random.randint(10, 25)
    critico = random.randint(1, 100)
    if critico <= 10:
        daño = daño * 2
        print("Has sacado un Golpe critico")
    return daño

def habilidad_especial():
    fallar = random.randint(1, 100)
    if fallar <=50:
        daño = 0
    else:
        daño = random.randint(30, 50)
    return daño
    
def generar_cura():
    global pociones
    global cura
    cura = random.randint(20, 20)
    pociones = pociones - 1        
    return cura

def mostrar_estado():
    print("\n╔══════════════════════════════════════╗")
    print(f"║  ❤️  {nombre_heroe}: {salud_heroe} HP")
    print(f"║  💀 {nombre_enemigo}: {salud_enemigo} HP")
    print("╚══════════════════════════════════════╝")

def verificar_ganador():
    
    if salud_heroe <= 0:
        print(f"{nombre_heroe} tú HP ha llegado a {salud_heroe}, has perdido.")
        ganador = True
        return ganador
    elif salud_enemigo <= 0:
        print("FELICIDADES HAS GANADO.")
        ganador = True
        return ganador
    else:
        return False
def turno_jugador():
        global mostrar    
        global salud_enemigo
        global salud_heroe
        turno_valido = False
        while not turno_valido:
            try:
                mostrar = int(input(f"\n==============================================\n1) Atacar (Daño 10 - 15) \n2) Curar({pociones})\n3) Habilidad especial (Daño 30 - 50)\n==============================================\nIngresa una opcion: ").strip())
            except:
                print("No se pueden colocar letras")
            if mostrar == 1:
                daño = generar_daño()
                print(f"╔══════════════════{nombre_heroe}════════════════════╗")
                print(f"║  ⚔️  ataca a {nombre_enemigo} (-{daño}HP)")
                print(f"╚══════════════════════════════════════╝")
                salud_enemigo = salud_enemigo - daño
                turno_valido = True
            elif mostrar == 2:
                if pociones <= 0:
                    print(f"╔═══════════════════{nombre_heroe}═══════════════════╗")
                    print(f"║  pociones: {pociones}, Lo siento, no puedes curarte ")
                    print(f"╚══════════════════════════════════════╝")
                    turno_valido = False
                else:
                    curar = generar_cura()
                    print(f"╔═══════════════════{nombre_heroe}═══════════════════╗")
                    print(f"║  Se ha curado ({curar}HP)")
                    print(f"╚══════════════════════════════════════╝")
                    salud_heroe = salud_heroe + curar
                    turno_valido = True
            elif mostrar == 3:
                DAÑO_HABILIDAD_ESPECIAL = habilidad_especial()
                print(f"╔═══════════════════{nombre_heroe}═══════════════════╗")
                print(f"║  Lanza habilidad especial : (-{DAÑO_HABILIDAD_ESPECIAL}HP)")
                print(f"╚══════════════════════════════════════╝")
                salud_enemigo = salud_enemigo - DAÑO_HABILIDAD_ESPECIAL
                turno_valido = True
            else:
                print("Opciones No es Valida")
                turno_valido = False
        
def turno_enemigo():
    global salud_heroe
    global salud_enemigo
    if salud_enemigo <= (salud_enemigo_max/100)*20:
        curar = generar_cura()
        print(f"╔═══════════════════{nombre_enemigo}═══════════════════╗")
        print(f"║  Se ha curado ({curar}HP)")
        print(f"╚══════════════════════════════════════╝")
        salud_enemigo =  salud_enemigo + curar
    else:
        daño = generar_daño()
        print(f"╔═══════════════════{nombre_enemigo}═══════════════════╗")
        print(f"║  🗡️  ataca a {nombre_heroe} (-{daño}HP)")
        print(f"╚══════════════════════════════════════╝")
        salud_heroe = salud_heroe - daño