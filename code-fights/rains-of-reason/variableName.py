def variableName(name):
    if name[0].isdigit():
        return False
    for i in range(len(name)):
        if not name[i].isalnum():
            if name[i] != "_":
                return False
    return True
