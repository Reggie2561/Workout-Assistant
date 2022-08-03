import random
import time
from timer import timer
import subprocess
import json
class session:
    def __init__(self, weight):
        self.weight = weight

    def pushup(self, max):
        sets = []
        pushingWieght = self.weight* 0.56
        for _ in range(5):
            sets.append(random.randint(round(0.65*max), max))
        return [sets, round(pushingWieght)]

    def pullups(self, max):
        sets = []
        for _ in range(5):
            sets.append(random.randint(round(0.60 * max), max))
        return sets

    def plank(self, Time):
        t = timer()
        conTime = t.convert(Time)
        t.start(conTime, Countdown=True)

    def squats(self, max):
        sets = []
        for _ in range(5):
            sets.append([random.randint(round(0.75 * max), max)], self.weight*0.75)
        return sets

    def running(self):
        stats = []
        num = 0
        pause = False
        print("Press CTRL C to pause")
        while True:
            try:
                if pause == True:
                    value = input("Press enter to continue\nOr type 's' to see run stats\n\n")
                    if value.lower() == "stop":
                        break
                    pause = False
                loc_data = subprocess.run(["termux-location", ], capture_output=True)

                data = json.loads(loc_data.stdout.decode())

                lat = data["latitude"]
                lon = data["longitude"]
                altitude = data["altitude"]
                speed = data["speed"]

                time.sleep(1)
                stats.append({"occurance": num, "lat": lat, "lon": lon, "altitude": altitude, "speed": speed})
                num += 1
            except KeyboardInterrupt:
                pause = True
            except Exception:
                pass

        return stats

    def rest(self, Time="1:30"):
        t = timer()
        conTime = t.convert(Time)
        t.start(conTime, Countdown=True, notifcation=True)
