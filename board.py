import random

class Board:
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[random.choice([0, 1]) for _ in range(cols)] 
                     for _ in range(rows)]
    
    def display(self):
        for row in self.grid:
            print("".join("██" if cell else "  " for cell in row))
        print()
    
    def count_neighbours(self, row, col):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i != 0 and j != 0 
                    and 0 <= row + i < self.rows and 0 <= col + j < self.cols):
                    count += self.grid[row + i][col + j]
        return count
    
    def update(self):
        NUM_REPRODUCE = 3
        MIN_SURVIVE = 2
        MAX_SURVIVE = 3

        newGrid = [[0] * self.cols for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                numNeighbours = self.count_neighbours(i, j)
                
                if (self.grid[i][j] and numNeighbours in (MIN_SURVIVE, MAX_SURVIVE)
                    or not self.grid[i][j] and numNeighbours == NUM_REPRODUCE):
                    newGrid[i][j] = 1

        self.grid = newGrid

