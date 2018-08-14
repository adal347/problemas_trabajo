BOARD = [[True, False, True, False, True, False, True, False],
         [False, True, False, True, False, True, False, True],
         [True, False, True, False, True, False, True, False],
         [False, True, False, True, False, True, False, True],
         [True, False, True, False, True, False, True, False],
         [False, True, False, True, False, True, False, True],
         [True, False, True, False, True, False, True, False],
         [False, True, False, True, False, True, False, True]]

def checkCol(col):
    if col == "A":
        return 0
    if col == "B":
        return 1
    if col == "C":
        return 2
    if col == "D":
        return 3
    if col == "E":
        return 4
    if col == "F":
        return 5
    if col == "G":
        return 6
    if col == "H":
        return 7

def chessBoardCellColor(cell1, cell2):
    col1 = checkCol(cell1[0])
    row1 = int(cell1[1]) - 1
    col2 = checkCol(cell2[0])
    row2 = int(cell2[1]) - 1

    if BOARD[row1][col1] == BOARD[row2][col2]:
        return True
    return False
