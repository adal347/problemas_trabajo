def constructShell(n):
    return [[0]*x for x in range(n)][1::]+[[0]*x for x in range(n+1)][:0:-1]
