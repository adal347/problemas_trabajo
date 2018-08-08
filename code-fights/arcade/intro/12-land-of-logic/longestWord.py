def longestWord(text):
    count = 0
    maximun = 0
    word = ""
    posibleWord = ""
    for value in text:
        if value.isalpha():
            count += 1
            posibleWord += value
        else:
            if maximun < count:
                word = posibleWord
                maximun = count
            count = 0
            posibleWord = ""
    if maximun < count:
        word = posibleWord
        maximun = count
    return word
