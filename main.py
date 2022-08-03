import os
from timer import timer
import platform
from workout import session
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
            set = workout.pushup(34)

            for i in set[0]:
                sys.stdout.write(f"Pushing weight is {set[1]}lbs\n")
                sys.stdout.write(f"Do {i} pushups\n")
                sys.stdout.write(f"Enter When Done\n")
                input("")

                if i == 5:
                    break
                sys.stdout.write("Starting 1:30 timer\n")
                workout.rest("1:30")


        elif o == "2":
            Time = input("How long of a plank? [0:00]: ")
            input("PRESS ENTER TO START...")
            workout.plank(Time)


        elif o == "3":
            max = input("Max amount Pullups you can do: ")
            set = workout.pullups(int(max))

            for rep in set:
                sys.stdout.write(f"Pulling weight is {workout.weight}\nDo {rep} pullups\nEnter When Done\n")
                sys.stdout.flush()
                input("")
                sys.stdout.write("Starting 1:30 timer\n")

                workout.rest("1:30")


        elif o == "4":
            pass


        elif o == "5":
            max = input("Max amount of squats you can do: ")

            set = workout.squats(int(max))

            for rep in set[0]:
                sys.stdout.write(f"Lifting weight is {max[1]}lbs\nDo {rep} squats\nEnter When Done\n")
                sys.stdout.flush()
                input("")
                sys.stdout.write("Starting 1:30 timer\n")

                workout.rest("1:30")


        elif o == "6":
            pass


        elif o == "7":
            pass


        elif o == "8":
            os.system(clear)
            results = workout.running()
            for item in results:
                print(item)

        input("Press ENTER to continue")
        main()
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