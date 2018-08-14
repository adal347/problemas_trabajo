NO_OF_CHARS = 256

def palindromeRearranging(inputString):
    count = [0] * NO_OF_CHARS
    for i in range(len(inputString)):
        count[ord(inputString[i])] = count[ord(inputString[i])] + 1
    odd = 0
    for i in range(NO_OF_CHARS):
        if count[i] & 1:
            odd += 1
        if odd > 1:
            return False
    return True
