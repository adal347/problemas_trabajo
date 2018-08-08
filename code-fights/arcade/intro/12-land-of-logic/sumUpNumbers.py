def sumUpNumbers(inputString):
    digit = ""
    suma = 0
    for value in inputString:
        if value.isdigit():
            digit += value
        else:
            if digit:
                suma += int(digit)
                digit = ""
    if digit:
        suma += int(digit)
    return suma
