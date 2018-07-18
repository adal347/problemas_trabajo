def hasNext(j, height):
    if j + 1 >= height:
        return False
    return True

def hasLowerCornerRight(i, j, width, height):
    if j + 1 >= height:
        return False
    if i + 1 >= width:
        return False
    return True

def hasDown(i, width):
    if i + 1 >= width:
        return False
    return True

def hasLowerCornerLeft(i, j, width):
    if j - 1 < 0:
        return False
    if i + 1 >= width:
        return False
    return True

def hasPrevious(j):
    if j - 1 < 0:
        return False
    return True

def hasUpperCornerLeft(i, j):
    if j - 1 < 0:
        return False
    if i - 1 < 0:
        return False
    return True

def hasUp(i):
    if i - 1 < 0:
        return False
    return True

def hasUpperCornerRight(i, j, height):
    if j + 1 >= height:
        return False
    if i - 1 < 0:
        return False
    return True

def check(matrix, i, j, width, height):
    count = 0
    if hasNext(j, height):
        if matrix[i][j + 1]:
            count += 1
    if hasLowerCornerRight(i, j, width, height):
        if matrix[i + 1][j + 1]:
            count += 1
    if hasDown(i, width):
        if matrix[i + 1][j]:
            count += 1
    if hasLowerCornerLeft(i, j, width):
        if matrix[i + 1][j - 1]:
            count += 1
    if hasPrevious(j):
        if matrix[i][j - 1]:
            count += 1
    if hasUpperCornerLeft(i, j):
        if matrix[i - 1][j - 1]:
            count += 1
    if hasUp(i):
        if matrix[i - 1][j]:
            count += 1
    if hasUpperCornerRight(i, j, height):
        if matrix[i - 1][j + 1]:
            count += 1
    return count

def minesweeper(matrix):
    board = []
    row = []
    width = len(matrix)
    for i  in range(width):
        height = len(matrix[i])
        for j in range(height):
            row.append(check(matrix, i, j, width, height))
        board.append(row)
        row = []
    return board
