def imageFilter(image, row, column):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            sum += image[row + i][column + j]
    return int(sum / 9)

def boxBlur(image):
    newImage = []
    height = len(image)
    width = len(image[0])
    for row in range(1, height - 1):
        newRow = []
        for column in range(1, width - 1):
            newRow.append(imageFilter(image, row, column))
        newImage.append(newRow)
    return newImage
