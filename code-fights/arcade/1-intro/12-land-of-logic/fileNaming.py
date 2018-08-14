def fileNaming(names):
    for i in range(len(names)):
        if names[i] in names[:i]:
            counter = 1
            while names[i] + "(" + str(counter) + ")" in names[:i]:
                counter += 1
            names[i] += "(" + str(counter) + ")"
    return names
