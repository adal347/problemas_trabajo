import datetime

def maliciousProgram(curDate, changes):
    time = datetime.datetime.strptime(curDate, '%d %b %Y %H:%M:%S')
    d, m, y, H, M, S = changes

    try:
        newTime = time.replace(year = time.year + y,
                                month = time.month + m,
                                day = time.day + d,
                                hour = time.hour + H,
                                minute = time.minute + M,
                                second = time.second + S)
    except ValueError as e:
        return curDate
    return newTime.strftime('%d %b %Y %H:%M:%S')
