import itertools

def adjacentNodes(string1, string2):
    count = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            count += 1
            if count > 1:
                return False
    if count == 1:
        return True
    else:
        return False

def stringsRearrangement(inputArray):
    permutations = list(itertools.permutations(inputArray))
    for value in permutations:
        for i in range(len(value) - 1):
            isAdjacent = adjacentNodes(value[i], value[i + 1])
            if not isAdjacent:
                break
        if isAdjacent:
            return True
    return False
