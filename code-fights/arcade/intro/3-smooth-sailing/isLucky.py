def isLucky(n):
    number = str(n)
    length = int(len(number)/2)
    first = number[0:length]
    second = number[length:len(number)]
    firstHalf = 0
    secondHalf = 0
    for i in range(len(first)):
        firstHalf += int(first[i])
        secondHalf += int(second[i])
    if firstHalf == secondHalf:
        return True
    return False
