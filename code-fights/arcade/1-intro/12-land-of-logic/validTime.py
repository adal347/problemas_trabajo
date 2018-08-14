def validTime(time):
    time = time.split(":")
    if int(time[0]) >= 24:
        return False
    if int(time[1]) >= 60:
        return False
    return True
