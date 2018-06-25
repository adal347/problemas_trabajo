def areSimilar(a, b):
    ids = []
    for i in range(len(a)):
        if a[i] != b[i]:
            ids.append(i)
    if len(ids) == 0:
        return True
    if len(ids) != 2:
        return False
    if a[ids[0]] == b[ids[1]] and a[ids[1]] == b[ids[0]]:
        return True
    return False
