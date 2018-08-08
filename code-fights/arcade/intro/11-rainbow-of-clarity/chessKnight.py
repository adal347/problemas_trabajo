def isRightUpUp(knight):
    move = [knight[0] + 1, knight[1] + 2]
    if move[0] < 105 and move[1] < 9:
        return True
    return False

def isRightUpDown(knight):
    move = [knight[0] + 2, knight[1] + 1]
    if move[0] < 105 and move[1] < 9:
        return True
    return False

def isRightDownUp(knight):
    move = [knight[0] + 2, knight[1] - 1]
    if move[0] < 105 and move[1] > 0:
        return True
    return False

def isRightDownDown(knight):
    move = [knight[0] + 1, knight[1] - 2]
    if move[0] < 105 and move[1] > 0:
        return True
    return False

def isLeftUpUp(knight):
    move = [knight[0] - 1, knight[1] + 2]
    if move[0] > 96 and move[1] < 9:
        return True
    return False

def isLeftUpDown(knight):
    move = [knight[0] - 2, knight[1] + 1]
    if move[0] > 96 and move[1] < 9:
        return True
    return False

def isLeftDownUp(knight):
    move = [knight[0] - 2, knight[1] - 1]
    if move[0] > 96 and move[1] > 0:
        return True
    return False

def isLeftDownDown(knight):
    move = [knight[0] - 1, knight[1] - 2]
    if move[0] > 96 and move[1] > 0:
        return True
    return False

def chessKnight(cell):
    knight = [ord(cell[0]), int(cell[1])]
    count = 0
    if isRightUpUp(knight):
        count += 1
    if isRightUpDown(knight):
        count += 1
    if isRightDownUp(knight):
        count += 1
    if isRightDownDown(knight):
        count += 1
    if isLeftUpDown(knight):
        count += 1
    if isLeftDownUp(knight):
        count += 1
    if isLeftDownDown(knight):
        count += 1
    if isLeftUpUp(knight):
        count += 1
    return count
