class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        from collections import Counter
        x = Counter(''.join([i[0].lower() for i in self.names]))
        y = Counter(''.join([i[-1].lower() for i in self.names]))
        z = (x - y) + (y-x)
        v = sum(z.values())
        return v == 2 or v == 0

def isCoolTeam(team):
    return bool(Team(team))
