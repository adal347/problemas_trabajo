def adjacentElementsProduct(inputArray):
    index = inputArray[0] * inputArray[1];
    for i in range(1, int(round(len(inputArray) - 1))):
        product = inputArray[i] * inputArray[i + 1]
        if product > index:
            index = product
    return index
