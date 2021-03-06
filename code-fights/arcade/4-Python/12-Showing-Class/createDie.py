import random

def createDie(seed, n):
    class Die(object):
        def __init__(self, seed, n):
            self.seed = seed
            self.n = n
            random.seed(self.seed)
            self.value = int(random.random() * self.n) + 1

        def __get__(self, instance, owner):
            return self.value

    class Game(object):
        die = Die(seed, n)

    return Game.die
