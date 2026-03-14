from board import Board
from GUI import GameOfLifeGUI

def main():
    # Customize these values to change the size of the board
    ROWS = 20
    COLS = 20

    # Initialize the board and GUI, then start the game loop
    board = Board(ROWS, COLS)
    gui = GameOfLifeGUI(board)
    gui.play()

if __name__ == "__main__":
    main()
