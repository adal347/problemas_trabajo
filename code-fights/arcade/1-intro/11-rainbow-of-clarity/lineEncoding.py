def lineEncoding(s):
    i = 0
    j = 0
    count = 0
    newS = ""
    while True:
        if s[i] == s[j]:
            count += 1
            j += 1
        else:
            if count == 1:
                newS += s[i]
            else:
                newS += str(count) + s[i]
            count = 0
            i = j
        if j == len(s):
            if count == 1:
                newS += s[i]
            else:
                newS += str(count) + s[i]
            break
    return newS
