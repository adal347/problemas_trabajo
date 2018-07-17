def evenDigitsOnly(n):
    number = str(n)
    for i in range(len(number)):
        digit = int(number[i])
        if digit % 2 != 0:
            return False
    return True
