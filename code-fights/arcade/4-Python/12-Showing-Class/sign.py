class Functions(object):
    def sign(x):
        if (x > 0):
            return 1
        elif (x < 0):
            return -1
        else:
            return 0

def sign(x):
    return Functions.sign(x)
