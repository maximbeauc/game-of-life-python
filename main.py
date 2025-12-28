from board import Board
import time

def main():
    ROWS = 10
    COLS = 10
    WAIT_TIME = 0.5

    board = Board(ROWS, COLS)

    while (True):
        board.display()
        board.update()
        time.sleep(WAIT_TIME)

if __name__ == "__main__":
    main()
