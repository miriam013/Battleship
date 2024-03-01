from Tablero import Tablero
from Jugador import Jugador

# ===================== JUEGO =====================

def game():
    hundir_la_flota()
    print("\t1 - 1 jugador")
    print("\t2 - 2 jugadores")
    opcion = input("\t\tIntroduce tu opcion --> ")

    if opcion == '1':
        one_player()
    elif opcion == '2':
        two_player()
    else:
        print("ADIOS :)")

def hundir_la_flota():
    print("--------------------------")
    print("| 🚢 Hundir la flota ⚓ |")
    print("--------------------------")

def one_player(): # Modo un jugador
    juego_en_proceso = True
    t_01 = Tablero()

    j_01 = Jugador("Jugador1", t_01)

    j_01.generar_barcos()

    while juego_en_proceso:
        if j_01.get_vida == 0:
            juego_en_proceso = False

        t_01.imprimir_tablero()

        print()
         
        juego_en_proceso = j_01.disparar()

    t_01.print_win(j_01)

    print()
    
def two_player(): # Modo dos jugadores
    juego_en_proceso = True
    turno = 1
   
    t_01 = Tablero()
    t_02 = Tablero()

    j_01 = Jugador("Jugador 1", t_01)
    j_02 = Jugador("Jugador 2", t_02)

    j_01.generar_barcos()
    j_02.generar_barcos()

    while juego_en_proceso:
        if turno == 1:
            if j_01.get_vida == 0:
                juego_en_proceso = False

            print()

            print(f"================ TURNO {j_01.get_nombre} ================", end="\n")
            
            juego_en_proceso = j_01.disparar()

            print()

            t_01.imprimir_tablero()

            print()

            turno = 2
        else:
            if j_02.get_vida == 0:
                juego_en_proceso = False
            
            print()

            print(f"================ TURNO {j_02.get_nombre} ================", end="\n")

            juego_en_proceso = j_02.disparar()

            print()

            t_02.imprimir_tablero()

            print()
            
            turno = 1

    print(f"================ TABLERO {j_01.get_nombre} ================")
    
    print()
    
    t_01.imprimir_tablero()
    
    print()
    
    print(f"================ TABLERO {j_02.get_nombre} ================")
    
    print()
    
    t_02.imprimir_tablero()

game()