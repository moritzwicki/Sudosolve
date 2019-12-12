import Tkinter as tk
import tkMessageBox
from Tkinter import IntVar


def drawGrid():
    root = tk.Tk()
    root.title("Easy Sudoku")
    b = tk.Button(root, text="Correct")
    b.grid(row=10, column=10)

    number_row = 0
    number_col_1 = 1
    number_col_2 = 1
    number_col_3 = 1
    number_col_4 = 1
    number_col_5 = 1
    number_col_6 = 1
    number_col_7 = 1
    number_col_8 = 1
    number_col_9 = 1
    while number_row <= 8:
        row_1 = tk.Entry(root, width=2)
        row_1.grid(row=number_row, column=0)
        number_row += 1
    while number_col_1 <= 8:
        col_1 = tk.Entry(root, width=2)
        col_1.grid(row=0, column=number_col_1)
        number_col_1 += 1

    while number_col_2 <= 8:
        col_1 = tk.Entry(root, width=2)
        col_1.grid(row=1, column=number_col_2)
        number_col_2 += 1

    while number_col_3 <= 8:
        col_1 = tk.Entry(root, width=2)
        col_1.grid(row=2, column=number_col_3)
        number_col_3 += 1

    while number_col_4 <= 8:
        col_1 = tk.Entry(root, width=2)
        col_1.grid(row=3, column=number_col_4)
        number_col_4 += 1

    while number_col_5 <= 8:
        col_1 = tk.Entry(root, width=2)
        col_1.grid(row=4, column=number_col_5)
        number_col_5 += 1

    while number_col_6 <= 8:
        col_1 = tk.Entry(root, width=2)
        col_1.grid(row=5, column=number_col_6)
        number_col_6 += 1

    while number_col_7 <= 8:
        col_1 = tk.Entry(root, width=2)
        col_1.grid(row=6, column=number_col_7)
        number_col_7 += 1

    while number_col_8 <= 8:
        col_1 = tk.Entry(root, width=2)
        col_1.grid(row=7, column=number_col_8)
        number_col_8 += 1

    while number_col_9 <= 8:
        col_1 = tk.Entry(root, width=2)
        col_1.grid(row=8, column=number_col_9)
        number_col_9 += 1


win = tk.Tk()
win.geometry('1100x700')
win.title("First Gui")

tk.Label(win, text="Herzlich Willkommen bei SudoSolve", font=("Arial Bold", 50)).pack()
tk.Label(win, text="Waehlen sie den Schwierigkeitsgrad des Sudokus", font=("Arial Bold", 20)).pack()
tk.Button(win, text="leicht", command=lambda: drawGrid()).pack()
tk.Button(win, text="Mittel").pack()
tk.Button(win, text="Schwierig").pack()
tk.Button(win, text="Extrem").pack()

win.mainloop()