def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        x, *res, z = res
    return res
