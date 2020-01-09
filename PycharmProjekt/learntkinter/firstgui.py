
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
win.configure(bg="DeepSkyBlue2")

tk.Label(win, text="Herzlich Willkommen bei SudoSolve", font=("Arial Bold", 50), bg="DeepSkyBlue2").pack()
tk.Label(win, text="Waehlen sie den Schwierigkeitsgrad des Sudokus", font=("Arial Bold", 20), bg="DeepSkyBlue2").pack()
tk.Button(win, text="leicht", command=lambda: dgE.drawGridEasy(dgE.entries), highlightbackground='DeepSkyBlue2').pack()
tk.Button(win, text="Mittel", command=lambda: dgM.drawGridMiddle(dgM.entries), highlightbackground='DeepSkyBlue2').pack()
tk.Button(win, text="Schwierig", command=lambda: dgH.drawGridHard(dgH.entries), highlightbackground='DeepSkyBlue2').pack()
tk.Button(win, text="Extrem", command=lambda: dgX.drawGridExpert(dgX.entries), highlightbackground='DeepSkyBlue2').pack()
tk.Button(win, text="SudokuSolver", command=lambda: ssG.drawGridSolver(ssG.entries), highlightbackground='DeepSkyBlue2').pack()

win.mainloop()
