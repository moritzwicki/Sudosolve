from Tkconstants import END
from tkinter import messagebox
board = ['4', '9', '6', '1', '5', '7', '8', '3', '2',
         '2', '1', '8', '3', '9', '6', '7', '4', '5',
         '7', '5', '3', '2', '8', '4', '1', '9', '6',
         '5', '3', '1', '6', '7', '2', '9', '8', '4',
         '6', '4', '9', '8', '3', '1', '2', '5', '7',
         '8', '2', '7', '5', '4', '9', '6', '1', '3',
         '9', '6', '2', '4', '1', '5', '3', '7', '8',
         '1', '8', '5', '7', '6', '3', '4', '2', '9',
         '3', '7', '4', '9', '2', '8', '5', '6', '1']


def getEingabenHard(entries):
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
