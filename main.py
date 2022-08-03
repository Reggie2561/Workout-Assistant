import os
import time
import subprocess
import json
from timer import timer
import platform
from workout import session
from notify import Notification
import sys
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
(8) Running [Termux]
""")
        o = input("Option: ")
        workout = session(148)
        if o == "1":
            reps = workout.pushup(34)

            for i in reps[0]:
                sys.stdout.write(f"Pushing weight is {reps[1]}lbs\n")
                sys.stdout.write(f"Do {i} pushups\n")
                sys.stdout.write(f"Enter When Done\n")
                input("")

                if i == 5:
                    break
                sys.stdout.write("Starting 1:30 timer\n")
                t.start(90, Countdown=True, notifcation=True)
        if o == "8":
            stats = []
            pause = False
            print("Press CTRL C to pause")
            while True:
                try:
                    if pause == True:
                        value = input("Press enter to continue\nOr type stop to see run stats")
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
                    stats.append([lat,lon,altitude,speed])
                except KeyboardInterrupt:
                    pause = True
        print(stats)
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