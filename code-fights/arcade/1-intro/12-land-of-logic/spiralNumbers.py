def spiralNumbers(n):
    directories = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    currentDirectory = 0
    currentPosistion = (0, 0)
    result = [[0 for i in range(n)] for j in range(n)]
    for i in range(1, n * n + 1):
        result[currentPosistion[0]][currentPosistion[1]] = i
        nextPosition = currentPosistion[0] + directories[currentDirectory][0], currentPosistion[1] + directories[currentDirectory][1]
        if not (0 <= nextPosition[0] < n and 0 <= nextPosition[1] < n and result[nextPosition[0]][nextPosition[1]] == 0):
            currentDirectory = (currentDirectory + 1) % 4
            nextPosition = currentPosistion[0] + directories[currentDirectory][0], currentPosistion[1] + directories[currentDirectory][1]
        currentPosistion = nextPosition
    return result
