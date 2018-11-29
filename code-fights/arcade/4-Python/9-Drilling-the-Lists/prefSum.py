def prefSum(a):
    return functools.reduce(lambda p, n: p + [p[-1] + n], a, [0])[1:]
