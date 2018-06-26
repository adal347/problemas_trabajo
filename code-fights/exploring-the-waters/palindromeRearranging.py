NO_OF_CHARS = 256

def palindromeRearranging(inputString):
    count = [0] * NO_OF_CHARS
    for i in range(len(inputString)):
        count[ord(inputString[i])] = count[ord(inputString[i])] + 1
    odd = 0
    for i in range(NO_OF_CHARS):
        if count[i] & 1:
            odd += 1
        if odd > 1:
            return False
    return True

if __name__ == '__main__':
    print(ord("a"))
    print(ord("b"))
    print(ord("c"))
    print(ord("d"))
    print(ord("e"))
    print(ord("f"))
    print(ord("g"))
    print(ord("h"))
    print(ord("i"))
    print(ord("j"))
    print(ord("k"))
    print(ord("p"))
    print(ord("s"))
    print(ord("t"))
    print(ord("u"))
    print(ord("v"))
    print(ord("w"))
    print(ord("x"))
    print(ord("y"))
    print(ord("z"))
