def absoluteValuesSumMinimization(a):
    value = a[len(a) - 1]
    count = 0
    for i in range(len(a)):
        count += abs(a[i] + a[i])
    for i in range(len(a)):
        sum1 = 0
        for j in range(len(a)):
            sum1 += abs(a[j] - a[i])
        if sum1 < count:
            count = sum1
            value = a[i]
    return value
