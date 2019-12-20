from Tkconstants import END
from aetypes import end

import tkinter as tk
from numpy import delete

board = ['9', '2', '6', '4', '3', '5', '7', '8', '1',
         '8', '5', '1', '2', '7', '6', '4', '3', '9',
         '4', '7', '3', '9', '8', '1', '5', '2', '6',
         '6', '8', '5', '7', '4', '9', '3', '1', '2',
         '7', '3', '4', '6', '1', '2', '9', '5', '8',
         '2', '1', '9', '3', '5', '8', '6', '7', '4',
         '5', '6', '8', '1', '9', '3', '2', '4', '7',
         '3', '4', '2', '8', '6', '7', '1', '9', '5',
         '1', '9', '7', '5', '2', '4', '8', '6', '3']


def getEingabenMiddle(entries):
    countCorrect = 0
    countFaults = 0

    for i in range(len(board)):
        correcting = entries[i].get()
        if correcting == board[i]:
            countCorrect += 1

        elif correcting != board[i]:
            countFaults += 1
            entries[i].delete(0, END)
