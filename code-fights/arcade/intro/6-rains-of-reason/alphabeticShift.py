def alphabeticShift(inputString):
    newString = ""
    for i in range(len(inputString)):
        code = ord(inputString[i])
        code += 1
        if code == 123:
            code = 97
        newString += chr(code)
    return newString
