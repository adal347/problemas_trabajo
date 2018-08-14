def growingPlant(upSpeed, downSpeed, desiredHeight):
    days = 1
    height = upSpeed
    while height < desiredHeight:
        height -= downSpeed
        height += upSpeed
        days += 1
    return days
