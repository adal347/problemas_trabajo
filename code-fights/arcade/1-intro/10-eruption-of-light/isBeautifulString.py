NO_OF_CHARS = 256

def isBeautifulString(inputString):
    count = [0] * NO_OF_CHARS
    for i in range(len(inputString)):
        count[ord(inputString[i])] += 1
    for i in range(NO_OF_CHARS - 1):
        if count[i + 1] > count[i] and i != 96:
            return False
    return True
