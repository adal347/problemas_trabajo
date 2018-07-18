def extractEachKth(inputArray, k):
    length = len(inputArray)
    newList = []
    j = 2
    th = k
    if k == 1:
        return newList
    if k > length:
        return inputArray
    for i in range(length):
        if i != th - 1:
            newList.append(inputArray[i])
        else:
            th = k * j
            j += 1
        if k > length:
            break
    return newList
