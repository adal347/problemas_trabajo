def avoidObstacles(inputArray):
    inputArray.sort()
    i = 0
    jump = 1
    while True:
        if inputArray[i] % jump != 0 and i != len(inputArray) - 1:
            i += 1
        elif inputArray[i] % jump != 0 and i == len(inputArray) - 1:
            break
        elif inputArray[i] % jump == 0:
            i = 0
            jump += 1
    return jump
