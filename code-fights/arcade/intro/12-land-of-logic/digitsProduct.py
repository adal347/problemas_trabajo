def digitsProduct(product):
    if product == 0:
        return 10
    elif product == 1:
        return 1

    n = []

    while 1 < product:
        for divisor in range(9, 1, -1):
            if product % divisor == 0:
                product /= divisor
                n.append(d)
                break
        else:
            return -1
    return int(''.join(map(str, sorted(n))))
