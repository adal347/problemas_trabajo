def arrayMaximalAdjacentDifference(inputArray):
    difference = 0
    for i in range(len(inputArray) - 1):
        absolute = abs(inputArray[i] - inputArray[i + 1])
        if absolute > difference:
            difference = absolute
    return difference
