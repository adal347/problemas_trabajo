import numpy
def arrayMaxConsecutiveSum(inputArray, k):
    maxSum = 0
    for i in range(len(inputArray) - (k - 1)):
        sum = 0
        sum = numpy.sum(inputArray[i:i+k])
        if sum > maxSum:
            maxSum = sum
    return maxSum
