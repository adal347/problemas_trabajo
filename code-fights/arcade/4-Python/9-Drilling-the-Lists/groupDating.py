def groupDating(male, female):
    return list(zip(*[(i,j) for i, j in zip(male,female) if i != j])) if list(zip(*[(i,j) for i, j in zip(male,female) if i != j])) != [] else [[], []]
