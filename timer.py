import os
import time
import sys
from notify import Notification
class timer:
    def start(self, s, Countdown=None, notifcation=False):
        if Countdown == True:
            num = 0
            while num <= s:
                sys.stdout.write(f"{s-num}s left");
                sys.stdout.flush()
                num += 1
                time.sleep(1)
                sys.stdout.write('\r' * len(f"{s-num}s left"))
                sys.stdout.flush()
                if notifcation == True:
                    Notification().send(title="Timer in python", content=f"{s-num}s left", length=1.5)

        else:
            start = time.perf_counter()
            while True:
                if time.perf_counter()-start > s:
                    return
                print(round(time.perf_counter()-start))
    def convert(self, Time):
        Time = Time.split(":")
        Time1 = int(Time[0])*60
        return Time1+int(Time[1])

    def unconvert(self, s):
        r = s%60
        if r <= 9:
            r = str(f"0{r}")
        t = s/60
        t = str(t).split(".")
        return f"{t[0]}:{r}"
