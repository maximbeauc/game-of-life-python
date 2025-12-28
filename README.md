# Conway's Game of Life (Python)

A simple implementation of Conway’s Game of Life written in Python.

This project was created to practice:
- Python programming
- Object-oriented design
- Using VS Code
- Version control with Git and GitHub

## How It Works
The board is represented as a 2D grid where:
- Alive cells are shown as `██`
- Dead cells are shown as `  `

The simulation updates based on Conway’s rules:
- A live cell survives with 2 or 3 neighbors
- A dead cell becomes alive with exactly 3 neighbors
- All other cells die or remain dead

## How to Run

Make sure Python 3 is installed, then run:

```bash
python main.py