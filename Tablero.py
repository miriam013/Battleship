from Barco import Barco
import random

# ===================== CLASE TABLERO =====================        

class Tablero:
    def __init__(self):
        self.__tablero_visible = self.genero_tablero()  # Tablero que ve el jugador
        self.__tablero_real = self.genero_tablero()     # Tablero "real"

    def genero_tablero(self):
        tablero = []
        for j in range(10):
            fila = ['🔵'] * 10
            tablero.append(fila)
        return tablero

    def imprimir_tablero(self):
        print("  ", end=" ")
        for i in range(1, 11):
            print(f"{i} ", end=" ")

        letras = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}

        for i in range(len(self.__tablero_visible)):
            fila = self.__tablero_visible[i]
            letra = letras[i]
            print("\n" + letra + " " + " ".join(fila), end=" ")
    
    def generar_barcos(self):
        barco_01_longitud_2 = Barco(2, "horizontal")
        barco_02_longitud_2 = Barco(2, "horizontal")
        barco_03_longitud_2 = Barco(2, "vertical")
        barco_04_longitud_2 = Barco(2, "vertical")

        barco_01_longitud_3 = Barco(3, "horizontal")
        barco_02_longitud_3 = Barco(3, "horizontal")
        barco_03_longitud_3 = Barco(3, "vertical")
        barco_04_longitud_3 = Barco(3, "vertical")

        barco_01_longitud_8 = Barco(8, "horizontal")
        barco_02_longitud_8 = Barco(8, "vertical")

        barcos = [
            barco_01_longitud_2, barco_02_longitud_2, barco_03_longitud_2, barco_04_longitud_2,
            barco_01_longitud_3, barco_02_longitud_3, barco_03_longitud_3, barco_04_longitud_3,
            barco_01_longitud_8, barco_02_longitud_8
        ]

        # AÑADIR BARCOS AL TABLERO
        for barco in barcos:
            barco_colocado = False
            while (not barco_colocado):
                fila = random.randint(0, 9)
                columna = random.randint(0, 9)
                orientacion = barco.orientacion
                barco_colocado = barco.colocar_en_tablero(self.__tablero_real, fila, columna, orientacion)

    def actualizar_tablero(self, fila, columna, nuevo_valor):
        self.__tablero_visible[fila][columna] = nuevo_valor

    def obtener_estado_casilla(self, fila, columna):
        return self.__tablero_real[fila][columna]

    def print_win(self, j1):
        print(f"{j1.get_nombre} HA GANADO 👑")
        
    def print_tocado(self):
        print("💥 TOCADO 💥") 

    def print_agua(self):
        print("🌊 AGUA 🌊") 