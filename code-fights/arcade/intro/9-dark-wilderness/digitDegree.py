def digitDegree(n):
    number = str(n)
    newN = 0
    if len(number) == 1:
        return 0
    for value in number:
        newN += int(value)
    if len(str(newN)) == 1:
        return 1
    else:
        return digitDegree(newN) + 1
