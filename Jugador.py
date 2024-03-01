
# ===================== CLASE JUGADOR =====================

class Jugador:

    def __init__(self, nombre, tablero):
        self.__nombre = nombre
        self.__tablero = tablero
        self.__vida = 36 # vida = longitud de todos los barcos juntos
        
    def generar_barcos(self):
        self.__tablero.generar_barcos()

    @property
    def get_nombre(self):
        return self.__nombre
    
    @property
    def get_vida(self):
        return self.__vida

    def disparar(self):
        
        print()

        coordenada = input("\tCOORDENADA (Ej: A1) --> ")

        print()

        # Verifico si la coordenada es una letra-numero
        if (len(coordenada) != 2 and len(coordenada) != 3) or (not coordenada[0].isalpha()) or (not coordenada[1:].isdigit()):
            print("Coordenada no valida (A-J)(1-10) --> Ej: A1")
        else:
            fila = ord(coordenada[0].upper()) - ord('A')
            columna = int(coordenada[1:]) - 1

            if (fila < 0) or (fila >= 10) or (columna < 0) or (columna >= 10):
                print("Coordenada fuera del rango")
            else:
                estado_casilla = self.__tablero.obtener_estado_casilla(fila, columna)

                if estado_casilla == '🛟':
                    self.__tablero.print_tocado()
                    self.__tablero.actualizar_tablero(fila, columna, '💥') 
                    self.__vida -= 1
                elif estado_casilla == '🔵': 
                    self.__tablero.print_agua()
                    self.__tablero.actualizar_tablero(fila, columna, '🌊') 
                else:
                    print("Disparo repetido")

                print()
        
        return self.__vida