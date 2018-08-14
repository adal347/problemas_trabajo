def deleteDigit(n):
    original = str(n)
    lenght = len(original)
    maximun = int(original[1:])
    for i in range(lenght):
        posible = int(original[:i] + original[i + 1:])
        maximun = max(maximun, posible)
    return maximun
