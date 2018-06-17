#!/usr/bin/env python3

import datetime


def set_pomodoro():
    """
    Set a pomodoro
    """
    pomodoro_count = 0

    value = int(input("Enter your desired time in minutes: "))

    time_now = datetime.datetime.now()
    print("\nThe time is {}".format(time_now))

    set_time = datetime.timedelta(minutes=value)

    delta = time_now + set_time
    print("The Pomodoro will finish at {}".format(delta))

    while True:
        if delta == datetime.datetime.now():
            print("Time up! {} minutes completed!".format(value))
            pomodoro_count += 1
            break

    print("Successfully completed {} pomodoro!".format(pomodoro_count))


if __name__ == "__main__":
    set_pomodoro()
