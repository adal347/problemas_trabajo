def alternatingSums(a):
    team1 = 0
    team2 = 0
    weigths = []
    for i in range(len(a)):
        if i % 2:
            team2 += a[i]
        else:
            team1 += a[i]
    weigths.append(team1)
    weigths.append(team2)
    return weigths
