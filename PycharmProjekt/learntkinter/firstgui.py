import array

import tkinter as tk
import tkMessageBox
from Tkinter import IntVar, Entry




def drawGrid():
    root = tk.Tk()
    entries = {}
    tableheight = 9
    tablewidth = 9
    counter = 0
    for row in xrange(tableheight):
        for column in xrange(tablewidth):
            entries[counter] = tk.Entry(root, width=2)
            entries[counter].grid(row=row, column=column)
            counter += 1
    print entries
    entries[11].insert(0,"2")
    entries[11].insert(0,"3")
win = tk.Tk()
win.geometry('1100x700')
win.title("First Gui")

tk.Label(win, text="Herzlich Willkommen bei SudoSolve", font=("Arial Bold", 50)).pack()
tk.Label(win, text="Waehlen sie den Schwierigkeitsgrad des Sudokus", font=("Arial Bold", 20)).pack()
tk.Button(win, text="leicht", command=lambda: drawGrid()).pack()
tk.Button(win, text="Mittel").pack()
tk.Button(win, text="Schwierig").pack()
tk.Button(win, text="Extrem").pack()




#def EntryOutput(rootIdentyfier, windowIdentifier, outputValue):
   # return rootIdentyfier.StringVar(windowIdentifier, value=outputValue)


#test = Entry(win, textvariable=EntryOutput(tk, win, "Work mf work")).pack()

win.mainloop()