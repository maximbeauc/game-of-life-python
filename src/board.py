import random

"""
A class to represent the game board for Conway's Game of Life.
"""
class Board:
    # The constructor initializes the board with a specified number of rows and columns,
    # and creates a grid filled with zeros (indicating dead cells).
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0] * cols for _ in range(rows)]
    
    # The display method prints the current state of the board to the console for debugging purposes, 
    # using "██" for alive cells and "  " for dead cells.
    def display(self):
        for row in self.grid:
            print("".join("██" if cell else "  " for cell in row))
        print()
    
    # The count_neighbours method counts the number of alive neighbors around a given cell (row, col).
    def count_neighbours(self, row, col):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if ((i != 0 or j != 0) 
                    and 0 <= row + i < self.rows and 0 <= col + j < self.cols):
                    count += self.grid[row + i][col + j]
        return count
    
    # The update method applies the rules of Conway's Game of Life to update the state of the board for the next generation.
    def update(self):
        NUM_REPRODUCE = 3
        MIN_SURVIVE = 2
        MAX_SURVIVE = 3

        newGrid = [[0] * self.cols for _ in range(self.rows)]

        # Iterate through each cell in the grid and determine its next state based on the number of alive neighbors.
        for i in range(self.rows):
            for j in range(self.cols):
                numNeighbours = self.count_neighbours(i, j)
                
                if (self.grid[i][j] and numNeighbours in (MIN_SURVIVE, MAX_SURVIVE)
                    or not self.grid[i][j] and numNeighbours == NUM_REPRODUCE):
                    newGrid[i][j] = 1

        self.grid = newGrid

