import tkinter as tk
import SudokuSolver as suso
entries = {}


def drawGridSolver(entries):
    root = tk.Tk()
    root.title("Sudoku")
    tableheight = 9
    tablewidth = 9
    counter = 0
    for row in xrange(tableheight):
        for column in xrange(tablewidth):
            entries[counter] = tk.Entry(root, width=2, justify='center')
            entries[counter].grid(row=row, column=column)
            counter += 1

    entries[0].configure(bg="cornsilk2")
    entries[1].configure(bg="cornsilk2")
    entries[2].configure(bg="cornsilk2")
    entries[6].configure(bg="cornsilk2")
    entries[7].configure(bg="cornsilk2")
    entries[8].configure(bg="cornsilk2")
    entries[9].configure(bg="cornsilk2")
    entries[10].configure(bg="cornsilk2")
    entries[11].configure(bg="cornsilk2")
    entries[15].configure(bg="cornsilk2")
    entries[16].configure(bg="cornsilk2")
    entries[17].configure(bg="cornsilk2")
    entries[18].configure(bg="cornsilk2")
    entries[19].configure(bg="cornsilk2")
    entries[20].configure(bg="cornsilk2")
    entries[24].configure(bg="cornsilk2")
    entries[25].configure(bg="cornsilk2")
    entries[26].configure(bg="cornsilk2")
    entries[30].configure(bg="cornsilk2")
    entries[31].configure(bg="cornsilk2")
    entries[32].configure(bg="cornsilk2")
    entries[39].configure(bg="cornsilk2")
    entries[40].configure(bg="cornsilk2")
    entries[41].configure(bg="cornsilk2")
    entries[48].configure(bg="cornsilk2")
    entries[49].configure(bg="cornsilk2")
    entries[50].configure(bg="cornsilk2")
    entries[54].configure(bg="cornsilk2")
    entries[55].configure(bg="cornsilk2")
    entries[56].configure(bg="cornsilk2")
    entries[60].configure(bg="cornsilk2")
    entries[61].configure(bg="cornsilk2")
    entries[62].configure(bg="cornsilk2")
    entries[63].configure(bg="cornsilk2")
    entries[64].configure(bg="cornsilk2")
    entries[65].configure(bg="cornsilk2")
    entries[69].configure(bg="cornsilk2")
    entries[70].configure(bg="cornsilk2")
    entries[71].configure(bg="cornsilk2")
    entries[72].configure(bg="cornsilk2")
    entries[73].configure(bg="cornsilk2")
    entries[74].configure(bg="cornsilk2")
    entries[78].configure(bg="cornsilk2")
    entries[79].configure(bg="cornsilk2")
    entries[80].configure(bg="cornsilk2")

    submitButton = tk.Button(root, text="Solve Sudoku", command= lambda: suso.SudokuSolving(entries))
    submitButton.grid(row=10, column=10)
