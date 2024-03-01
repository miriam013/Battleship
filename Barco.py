
# ===================== CLASE BARCO =====================

class Barco:

    def __init__(self, longitud, orientacion):
        self.longitud = longitud
        self.posicion = []
        self.orientacion = orientacion
        self.vida = longitud

    def colocar_en_tablero(self, tablero, fila, columna, orientacion):
        final_fila = fila
        final_columna = columna
        
        if orientacion == "horizontal":
            final_columna += self.longitud  
        else:
            final_fila += self.longitud 
        
        # Comprobamos si el barco se sale del tablero.
        if final_fila > len(tablero) or final_columna > len(tablero[0]):
            return False

        # Comprobamos si el espacio está libre para colocar el barco.
        for i in range(self.longitud):
            if orientacion == "horizontal" and tablero[fila][columna + i] != '🔵':
                return False
            elif orientacion == "vertical" and tablero[fila + i][columna] != '🔵':
                return False

        # Colocamos el barco en el tablero.
        for i in range(self.longitud):
            if orientacion == "horizontal":
                tablero[fila][columna + i] = '🛟'
            else:
                tablero[fila + i][columna] = '🛟'
            
        return True

    def colocar_en_tablero(self, tablero, fila, columna, orientacion):
        # Verifico que el barco no se salga del tablero
        if orientacion == "horizontal":
            if (columna + self.longitud) > len(tablero[0]):
                return False
            if any(tablero[fila][columna + i] != '🔵' for i in range(self.longitud)):
                return False
            for i in range(self.longitud):
                tablero[fila][columna + i] = '🛟'
        elif orientacion == "vertical":
            if fila + self.longitud > len(tablero):
                return False
            if any(tablero[fila + i][columna] != '🔵' for i in range(self.longitud)):
                return False
            for i in range(self.longitud):
                tablero[fila + i][columna] = '🛟'
        return True