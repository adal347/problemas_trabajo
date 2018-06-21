def allLongestStrings(inputArray):
    maxLength = 0
    newArray = []
    for value in inputArray:
        if len(value) > maxLength:
            newArray = []
            maxLength = len(value)
            newArray.append(value)
        elif len(value) == maxLength:
            newArray.append(value)
    return newArray
