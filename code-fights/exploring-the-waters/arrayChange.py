def arrayChange(inputArray):
    count = 0
    for i in range(len(inputArray) - 1):
        if inputArray[i] >= inputArray[i + 1]:
            x = inputArray[i] - inputArray[i + 1]
            x += 1
            inputArray[i + 1] = x
            count += x
            x = 0
    return count
