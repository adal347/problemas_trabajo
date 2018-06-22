def sortByHeight(a):
    tree = []
    a2 = []
    for i in range(len(a)):
        if a[i] == -1:
            tree.append(i)
        else:
            a2.append(a[i])
    a2.sort()
    for value in tree:
        a2.insert(value, -1)
    return a2
