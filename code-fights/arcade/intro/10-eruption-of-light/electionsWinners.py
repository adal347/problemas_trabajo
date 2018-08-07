def electionsWinners(votes, k):
    maximo = max(votes)
    count = 0
    aux = 0
    for value in votes:
        if value + k > maximo:
            count += 1
        if maximo == value:
            aux += 1
    if aux == 1 and count == 0:
        return 1
    return count
