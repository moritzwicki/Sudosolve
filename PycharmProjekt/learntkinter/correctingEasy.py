from Tkconstants import END
from tkinter import messagebox
board = ['7', '1', '8', '3', '4', '9', '6', '5', '2', '9', '5', '2', '1', '6', '7', '4', '8', '3', '4', '6', '3', '5',
         '2', '8', '7', '9', '1', '5', '7', '4', '2', '1', '3', '9', '6', '8', '8', '3', '9', '7', '5', '6', '1', '2',
         '4', '6', '2', '1', '8', '9', '4', '5', '3', '7', '2', '4', '7', '9', '3', '5', '8', '1', '6', '3', '9', '6',
         '4', '8', '1', '2', '7', '5', '1', '8', '5', '6', '7', '2', '3', '4', '9']


def getEingabenEasy(entries):
    countCorrect = 0
    countFaults = 0

    for i in range(len(board)):
        correcting = entries[i].get()
        if correcting == board[i]:
            countCorrect += 1

        elif correcting != board[i]:
            countFaults += 1
            entries[i].delete(0, END)

    if countCorrect == 81:
        messagebox.showinfo("Gewonnen", "Du hast das Sudoku geschafft!")
