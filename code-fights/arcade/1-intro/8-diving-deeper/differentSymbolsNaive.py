NO_OF_CHARS = 256

def differentSymbolsNaive(s):
    count = [0] * NO_OF_CHARS
    for i in range(len(s)):
        count[ord(s[i])] = count[ord(s[i])] + 1
    odd = 0
    for i in range(NO_OF_CHARS):
        if count[i] > 0:
            odd += 1
    return odd
