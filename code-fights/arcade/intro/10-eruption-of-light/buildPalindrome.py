def buildPalindrome(st):
    if st == st[::-1]:
        return st
    for i in range(len(st)):
        newSt = st + st[i::-1]
        if newSt == newSt[::-1]:
            return newSt
