def isIPv4Address(inputString):
    ip = inputString.split(".");
    if len(ip) != 4:
        return False
    for value in ip:
        if not value.isnumeric():
            return False
        number = int(value)
        if (255 - number) < 0:
            return False
    return True
