import os
import sys

from timer import timer
import platform
from workout import session
from notify import Notification

totalTime = 0


if platform.system() == "Windows":
    clear = "cls"
else:
    clear = "clear"


def main():
    os.system(clear)
    t = timer()
    print("""(1) Workout
(2) Timer
(3) Past Workouts
(99) Exit Program
""")
    o = input("Option: ")
    os.system(clear)
    if o == "1":
        print("""
(1) Pushups
(2) Pullups
(3) Planks
(4) Bicep Curls [NOT AVAILABLE YET]
(5) Squats [NOT AVAILABLE YET]
(6) Forearm Curls [NOT AVAILABLE YET]
(7) Shoulders [NOT AVAILABLE YET]
(8) Running [NOT AVAILABLE YET]
""")
        o = input("Option: ")
    elif o == "2":
        Time = input("Time [00:00]: ")
        conTime = t.convert(Time)
        t.start(conTime, Countdown=True)
        input("TIME IS UP!!!!\nENTER TO CONTINUE")
        main()
    elif o == "3":
        main()
    elif o == "99":
        exit()
if __name__ == '__main__':
    main()





    # global totalTime
    # start = time.perf_counter()
    #
    # t = timer()
    # print(f"Total Time = {t.unconvert(round(totalTime))}")
    # Time = input("Enter Time [00:00]: ")
    #
    # conTime = t.convert(Time)
    #
    # end = time.perf_counter()
    #
    # totalTime += conTime
    # totalTime += end-start
    #
    # t.start(conTime)