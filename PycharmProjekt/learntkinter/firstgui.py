import array
import sudokugenerator as sg
import tkinter as tk
import correctingEasy as cor

entries = {}


def drawGrid():
    root = tk.Tk()
    tableheight = 9
    tablewidth = 9
    counter = 0
    for row in xrange(tableheight):
        for column in xrange(tablewidth):
            entries[counter] = tk.Entry(root, width=2)
            entries[counter].grid(row=row, column=column)
            counter += 1
    sg.createEasy(entries)
    entries[0].configure(bg="azure")
    entries[1].configure(bg="azure")
    entries[2].configure(bg="azure")
    entries[6].configure(bg="azure")
    entries[7].configure(bg="azure")
    entries[8].configure(bg="azure")
    entries[9].configure(bg="azure")
    entries[10].configure(bg="azure")
    entries[11].configure(bg="azure")
    entries[15].configure(bg="azure")
    entries[16].configure(bg="azure")
    entries[17].configure(bg="azure")
    entries[18].configure(bg="azure")
    entries[19].configure(bg="azure")
    entries[20].configure(bg="azure")
    entries[24].configure(bg="azure")
    entries[25].configure(bg="azure")
    entries[26].configure(bg="azure")
    entries[30].configure(bg="azure")
    entries[31].configure(bg="azure")
    entries[32].configure(bg="azure")
    entries[39].configure(bg="azure")
    entries[40].configure(bg="azure")
    entries[41].configure(bg="azure")
    entries[48].configure(bg="azure")
    entries[49].configure(bg="azure")
    entries[50].configure(bg="azure")
    entries[54].configure(bg="azure")
    entries[55].configure(bg="azure")
    entries[56].configure(bg="azure")
    entries[60].configure(bg="azure")
    entries[61].configure(bg="azure")
    entries[62].configure(bg="azure")
    entries[63].configure(bg="azure")
    entries[64].configure(bg="azure")
    entries[65].configure(bg="azure")
    entries[69].configure(bg="azure")
    entries[70].configure(bg="azure")
    entries[71].configure(bg="azure")
    entries[72].configure(bg="azure")
    entries[73].configure(bg="azure")
    entries[74].configure(bg="azure")
    entries[78].configure(bg="azure")
    entries[79].configure(bg="azure")
    entries[80].configure(bg="azure")


    submitButton = tk.Button(root, text="Correcting", command=lambda: cor.geteingaben(entries))
    submitButton.grid(row=10, column=10)

    cor.geteingaben(entries)


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
