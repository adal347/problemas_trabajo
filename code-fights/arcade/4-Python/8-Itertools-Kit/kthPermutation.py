from itertools import permutations

def kthPermutation(numbers, k):
    return list(list(permutations(numbers))[k - 1])
