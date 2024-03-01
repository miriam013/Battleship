# Hundir la Flota 🚢⚓

## Contenido

1. [Estructura del Proyecto](#estructura-del-proyecto)
2. [Cómo Jugar](#cómo-jugar)
3. [Clases y Funciones](#clases-y-funciones)
4. [Instrucciones de Ejecución](#instrucciones-de-ejecución)

## Estructura del Proyecto

El proyecto sigue una estructura básica de clases para representar jugadores, barcos y tableros. Aquí hay una descripción general de las clases:

- **Barco:** Representa un barco con propiedades como longitud, orientación y posición.
- **Tablero:** Representa el tablero de juego con matrices para el tablero visible y el tablero real.
- **Jugador:** Representa un jugador con un nombre, un tablero y puntos de vida.

## Cómo Jugar

El juego puede ser jugado en dos modos:
- **Un Jugador:** Intenta hundir los barcos generados automáticamente en el tablero.
- **Dos Jugadores:** Los jugadores se turnan para disparar a los barcos del otro.

## Clases y Funciones

- **Barco:**
  - `__init__(self, longitud, orientacion)`: Inicializa un barco con longitud y orientación.
  - `colocar_en_tablero(self, tablero, fila, columna, orientacion)`: Coloca el barco en el tablero.

- **Tablero:**
  - `__init__(self)`: Inicializa el tablero con matrices para el tablero visible y el tablero real.
  - `genero_tablero(self)`: Genera un tablero lleno de '🔵'.
  - `imprimir_tablero(self)`: Muestra el tablero visible al jugador.
  - `generar_barcos(self)`: Crea instancias de barcos y los coloca en el tablero real.

- **Jugador:**
  - `__init__(self, nombre, tablero)`: Inicializa un jugador con nombre, tablero y puntos de vida.
  - `generar_barcos(self)`: Coloca los barcos en el tablero del jugador.
  - `get_nombre`: Devuelve el nombre del jugador.
  - `get_vida`: Devuelve los puntos de vida del jugador.
  - `disparar(self)`: Permite al jugador realizar un disparo.

- **Funciones de Juego:**
  - `game()`: Inicia el juego y permite al usuario elegir entre un jugador o dos jugadores.
  - `hundir_la_flota()`: Imprime el título del juego.
  - `one_player()`: Modo de un jugador.
  - `two_player()`: Modo de dos jugadores.
