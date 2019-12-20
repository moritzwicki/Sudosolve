
import tkinter as tk
import DrawGridMiddle as dgM
import DrawGridEasy as dgE
import DrawGridHard as dgH
import DrawGridExpert as dgX
import SudokuSolveGrid as ssG

#cor.geteingaben(dg.entries)

win = tk.Tk()
win.geometry('1100x700')
win.title("SudoSolve")

tk.Label(win, text="Herzlich Willkommen bei SudoSolve", font=("Arial Bold", 50)).pack()
tk.Label(win, text="Waehlen sie den Schwierigkeitsgrad des Sudokus", font=("Arial Bold", 20)).pack()
tk.Button(win, text="leicht", command=lambda: dgE.drawGridEasy(dgE.entries)).pack()
tk.Button(win, text="Mittel", command=lambda: dgM.drawGridMiddle(dgM.entries)).pack()
tk.Button(win, text="Schwierig", command=lambda: dgH.drawGridHard(dgH.entries)).pack()
tk.Button(win, text="Extrem", command=lambda: dgX.drawGridExpert(dgX.entries)).pack()
tk.Button(win, text="SudokuSolver", command=lambda: ssG.drawGridSolver(ssG.entries)).pack()

win.mainloop()
