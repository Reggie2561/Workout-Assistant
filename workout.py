import random
import time
from timer import timer

class session:
    def __init__(self, weight):
        self.weight = weight

    def pushup(self, max):
        sets = []
        pushingWieght = self.weight* 0.56
        for _ in range(5):
            sets.append(random.randint(round(0.65*max), max))
        return [sets, round(pushingWieght)]

    def Pullups(self, max):
        sets = []
        for _ in range(5):
            sets.append(random.randint(round(0.60 * max), max))
        return sets

    def plank(self, Time):
        t = timer()
        conTime = t.convert(Time)
        t.start(conTime, Countdown=True)

    def rest(self, Time="1:30"):
        t = timer()
        conTime = t.convert(Time)
        t.start(conTime, Countdown=True)
