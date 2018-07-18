def makeArrayConsecutive2(statues):
    mini = min(statues)
    maxi = max(statues)
    n = 0
    if mini == maxi:
        return n;
    for value in range(mini, maxi):
        if value not in statues:
            n += 1
    return n
