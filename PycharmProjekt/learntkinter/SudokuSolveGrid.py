import tkinter as tk
import SudokuSolver as suso

entries = {}


def drawGridSolver(entries):
    root = tk.Tk()
    root.title("Sudoku")

    GRIDSIZE = 9
    fullSet = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    # Create Possible values of 1..9 for each Cell
    for row in range(0, GRIDSIZE):
        for col in range(0, GRIDSIZE):
            if entries[row][col] == 0:
                # Create possible values in row and subtract from full set
                r = fullSet - set(entries[row])
                # Create possible values in column and subtract
                c = r - set(entries[:, col])
                # Create possible values in cube and subtract
                rowStart = (row // 3) * 3
                colStart = (col // 3) * 3
                entries[row][col] = list(c - set(entries[rowStart:rowStart + 3, colStart:colStart + 3].flatten()))
WA