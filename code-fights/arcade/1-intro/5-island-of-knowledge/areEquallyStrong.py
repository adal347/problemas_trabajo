def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft >= yourRight:
        yourStrongest = yourLeft
        yourWeakest = yourRight
    else:
        yourStrongest = yourRight
        yourWeakest = yourLeft
    if friendsLeft >= friendsRight:
        friendsStrongest = friendsLeft
        friendsWeakest = friendsRight
    else:
        friendsStrongest = friendsRight
        friendsWeakest = friendsLeft
    if yourStrongest == friendsStrongest and yourWeakest == friendsWeakest:
        return True
    else:
        return False
