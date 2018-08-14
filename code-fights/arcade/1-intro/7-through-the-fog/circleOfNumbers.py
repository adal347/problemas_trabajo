def circleOfNumbers(n, firstNumber):
    if firstNumber >= n/2:
        index = firstNumber - (n/2)
    else:
        index = firstNumber + (n/2)
    return index
