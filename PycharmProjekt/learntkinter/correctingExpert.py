from Tkconstants import END

board = ['1', '8', '5', '7', '3', '6', '4', '9', '2',
         '9', '6', '2', '4', '5', '1', '3', '8', '7',
         '3', '7', '4', '9', '8', '2', '5', '1', '6',
         '8', '2', '7', '5', '9', '4', '6', '3', '1',
         '5', '3', '1', '6', '2', '7', '9', '4', '8',
         '6', '4', '9', '8', '1', '3', '2', '7', '5',
         '4', '9', '6', '1', '7', '5', '8', '2', '3',
         '2', '1', '8', '3', '6', '9', '7', '5', '4',
         '7', '5', '3', '2', '4', '8', '1', '6', '9']


def getEingabenExpert(entries):
    countCorrect = 0
    countFaults = 0

    for i in range(len(board)):
        correcting = entries[i].get()
        if correcting == board[i]:
            countCorrect += 1

        elif correcting != board[i]:
            countFaults += 1
            entries[i].delete(0, END)
