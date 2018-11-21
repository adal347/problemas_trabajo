from itertools import product

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted([y for y in [createNumber(x) for x in list(product(digits, repeat = k))] if int(y)%d == 0])
