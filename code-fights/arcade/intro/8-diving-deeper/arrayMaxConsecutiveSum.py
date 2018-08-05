def arrayMaxConsecutiveSum(inputArray, k):
    maxSum = currentSum = sum(inputArray[:k])

    for i in range(len(inputArray) - k):
        currentSum = currentSum + inputArray[i + k] - inputArray[i]
        maxSum = max(currentSum, maxSum)

    return maxSum
