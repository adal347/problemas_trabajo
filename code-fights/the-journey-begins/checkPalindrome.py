def checkPalindrome(inputString):
    j = len(inputString) - 1
    for i in range(0, int(round(len(inputString)/2))):
        if (inputString[i] != inputString[j]):
            return False
        j -= 1
    return True
