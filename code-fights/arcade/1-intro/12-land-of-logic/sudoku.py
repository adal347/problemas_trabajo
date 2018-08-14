def duplicate(row):
    seen = set()
    for value in row:
        if value not in seen:
            seen.add(value)
        else:
            print(value)
            print(row)
            return True
    return False

def duplicateSquares(grid):
    listing = []
    for i in range(0, len(grid) - 2, 3):
        for j in range(0, len(grid[i]) - 2, 3):
            listing.append((grid[i][j], grid[i][j + 1], grid[i][j + 2],
                         grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2],
                        grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]))
    for value in listing:
        print(value)
        isDuplicate = duplicate(value)
        if isDuplicate:
            return False
    return True


def sudoku(grid):
    for i in range(9):
        isDuplicate = duplicate(grid[i])
        if isDuplicate:
            return False
        column = []
        for j in range(9):
            column.append(grid[j][i])
        isDuplicate = duplicate(column)
        if isDuplicate:
            return False
    return duplicateSquares(grid)
