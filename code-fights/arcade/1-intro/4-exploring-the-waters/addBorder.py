def addBorder(picture):
    length = len(picture[0]) + 2
    border = []
    up = "*" * length
    border.append(up)
    for value in picture:
        value = "*" + value + "*"
        border.append(value)
    border.append(up)
    return border

if __name__ == '__main__':
    print(addBorder(["abc", "ded"]))
