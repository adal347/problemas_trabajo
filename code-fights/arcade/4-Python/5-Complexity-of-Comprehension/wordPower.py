def wordPower(word):
    num = dict([(i, ord(i)-96) for i in word])
    return sum([num[ch] for ch in word])
