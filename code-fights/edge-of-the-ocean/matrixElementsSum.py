def matrixElementsSum(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                if i + 1 < len(matrix):
                    matrix[i + 1][j] = 0
            sum += matrix[i][j]
    return sum
