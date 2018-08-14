def longestDigitsPrefix(inputString):
    newString = ""
    if inputString[0].isdigit():
        for value in inputString:
            if value.isdigit():
                newString += value
            else:
                return newString
    return newString
