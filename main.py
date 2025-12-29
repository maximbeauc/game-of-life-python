from board import Board
from GUI import GameOfLifeGUI

def main():
    ROWS = 20, COLS = 20

    board = Board(ROWS, COLS)
    gui = GameOfLifeGUI(board)
    gui.play()

if __name__ == "__main__":
    main()
