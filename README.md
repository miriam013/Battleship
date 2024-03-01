# Battleship 🚢⚓

## Contents

1. [Project Structure](#project-structure)
2. [How to Play](#how-to-play)
3. [Classes and Functions](#classes-and-functions)

## Project Structure

The project follows a basic class structure to represent players, ships, and boards. Here is a general overview of the classes:

- **Ship:** Represents a ship with properties such as length, orientation, and position.
- **Board:** Represents the game board with matrices for the visible and real boards.
- **Player:** Represents a player with a name, a board, and life points.

## How to Play

The game can be played in two modes:
- **Single Player:** Try to sink automatically generated ships on the board.
- **Two Players:** Players take turns shooting at each other's ships.

## Classes and Functions

- **Ship:**
  - `__init__(self, length, orientation)`: Initializes a ship with length and orientation.
  - `place_on_board(self, board, row, column, orientation)`: Places the ship on the board.

- **Board:**
  - `__init__(self)`: Initializes the board with matrices for the visible and real boards.
  - `generate_board(self)`: Generates a board filled with '🔵'.
  - `print_board(self)`: Displays the visible board to the player.
  - `generate_ships(self)`: Creates instances of ships and places them on the real board.

- **Player:**
  - `__init__(self, name, board)`: Initializes a player with a name, a board, and life points.
  - `generate_ships(self)`: Places ships on the player's board.
  - `get_name`: Returns the player's name.
  - `get_life`: Returns the player's life points.
  - `shoot(self)`: Allows the player to take a shot.

- **Game Functions:**
  - `game()`: Starts the game and lets the user choose between single player or two players.
  - `sink_the_fleet()`: Prints the title of the game.
  - `single_player()`: Single-player mode.
  - `two_players()`: Two-player mode.
