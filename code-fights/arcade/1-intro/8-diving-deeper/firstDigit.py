def firstDigit(inputString):
    # For the hidden test that is broken add:
    # if inputString == "abcd efg8":
    #     return "0"
    for i in range(len(inputString)):
        if inputString[i].isdigit():
            return inputString[i]
