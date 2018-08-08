def isMAC48Address(inputString):
    ip = inputString.split("-");
    if len(ip) != 6:
        return False
    for value in ip:
        if len(value) != 2:
            return False
        if not all(hexa in string.hexdigits for hexa in value):
            return False
    return True
