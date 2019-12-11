# coding=utf-8
import tkinter as tk
import tkMessageBox
import argparse

win = tk.Tk()
win.geometry('1100x700')
win.title("First Gui")

def getsudoview():
    tkMessageBox.showinfo("Hello World", "Hallo Moritz die musst mal schwitzen")
    getsudoview()

tk.Label(win, text="Herzlich Willkommen bei SudoSolve", font=("Arial Bold", 50)).pack()
tk.Label(win, text="Wählen sie den Schwierigkeitsgrad des Sudokus", font=("Arial Bold", 20)).pack()
tk.Button(win, text="leicht", command = getsudoview).pack()
tk.Button(win, text="Mittel").pack()
tk.Button(win, text="Schwierig").pack()
tk.Button(win, text="Extrem").pack()

win.mainloop()
