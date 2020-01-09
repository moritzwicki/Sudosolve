import tkinter as tk
from Tkconstants import END


def sudosolve(entries, root):
    init = 0
    for init in range(len(entries)):
        if entries[init] != "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
            entries[init].insert(0, "0")
    grid = [[int(entries[0].get()), int(entries[1].get()), int(entries[2].get()), int(entries[3].get()),
             int(entries[4].get()), int(entries[5].get()), int(entries[6].get()), int(entries[7].get()),
             int(entries[8].get())], [
                int(entries[9].get()), int(entries[10].get()), int(entries[11].get()), int(entries[12].get()),
                int(entries[13].get()), int(entries[14].get()), int(entries[15].get()), int(entries[16].get()),
                int(entries[17].get())], [
                int(entries[18].get()), int(entries[19].get()), int(entries[20].get()), int(entries[21].get()),
                int(entries[22].get()), int(entries[23].get()), int(entries[24].get()), int(entries[25].get()),
                int(entries[26].get())], [
                int(entries[27].get()), int(entries[28].get()), int(entries[29].get()), int(entries[30].get()),
                int(entries[31].get()), int(entries[32].get()), int(entries[33].get()), int(entries[34].get()),
                int(entries[35].get())], [
                int(entries[36].get()), int(entries[37].get()), int(entries[38].get()), int(entries[39].get()),
                int(entries[40].get()), int(entries[41].get()), int(entries[42].get()), int(entries[43].get()),
                int(entries[44].get())], [
                int(entries[45].get()), int(entries[46].get()), int(entries[47].get()), int(entries[48].get()),
                int(entries[49].get()), int(entries[50].get()), int(entries[51].get()), int(entries[52].get()),
                int(entries[53].get())], [
                int(entries[54].get()), int(entries[55].get()), int(entries[56].get()), int(entries[57].get()),
                int(entries[58].get()), int(entries[59].get()), int(entries[60].get()), int(entries[61].get()),
                int(entries[62].get())], [
                int(entries[63].get()), int(entries[64].get()), int(entries[65].get()), int(entries[66].get()),
                int(entries[67].get()), int(entries[68].get()), int(entries[69].get()), int(entries[70].get()),
                int(entries[71].get())], [
                int(entries[72].get()), int(entries[73].get()), int(entries[74].get()), int(entries[75].get()),
                int(entries[76].get()), int(entries[77].get()), int(entries[78].get()), int(entries[79].get()),
                int(entries[80].get())]]

    # A function to check if the grid is full
    def checkGrid(grid):
        for row in range(0, 9):
            for col in range(0, 9):
                if grid[row][col] == 0:
                    return False

        # We have a complete grid!
        return True

    # A backtracking/recursive function to check all possible combinations of numbers until a solution is found
    def solveGrid(grid):
        # Find next empty cell
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if grid[row][col] == 0:
                for value in range(1, 10):
                    # Check that this value has not already be used on this row
                    if not (value in grid[row]):
                        # Check that this value has not already be used on this column
                        if not value in (
                                grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col],
                                grid[6][col],
                                grid[7][col], grid[8][col]):
                            # Identify which of the 9 squares we are working on
                            square = []
                            if row < 3:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(0, 3)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(0, 3)]
                                else:
                                    square = [grid[i][6:9] for i in range(0, 3)]
                            elif row < 6:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(3, 6)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(3, 6)]
                                else:
                                    square = [grid[i][6:9] for i in range(3, 6)]
                            else:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(6, 9)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(6, 9)]
                                else:
                                    square = [grid[i][6:9] for i in range(6, 9)]
                            # Check that this value has not already be used on this 3x3 square
                            if not value in (square[0] + square[1] + square[2]):
                                grid[row][col] = value
                                if checkGrid(grid):
                                    print("Grid Complete and Checked")
                                    return True
                                else:
                                    if solveGrid(grid):
                                        return True
                break
        print("Backtrack")
        grid[row][col] = 0

    solved = solveGrid(grid)
    if solved:
        print(grid)
        fieldPrint(grid, entries)
    else:
        print("Cannot Solve Sudoku Grid")





def fieldPrint(Array, entries):
    tmp354 = 0
    A = 0
    e = 0
    for i in range(81):
        if i % 9 == 0 and i != 0:
            tmp354 += 1
            A = 0

        toFill = str(Array[tmp354][A])
        entries[i].insert(0, toFill)
        entries[i].delete(1, END)
        A += 1

