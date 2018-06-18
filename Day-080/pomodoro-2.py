#!/usr/bin/env python3

# Pybites #100DaysofChallenge third day Challenge
# Create a Pomodoro application

import datetime
import sys

pomodoro_count = 0


def set_pomodoro():
    """
    Set a pomodoro
    """
    print("\n{:^50}".format("- Pomodoro Timer -"))

    # 1. Counter to note the pomodoros
    # Global var set, so as to not be cleared while being updated.
    global pomodoro_count

    # 2. Safety checks
    value = input("\nEnter your time in minutes: ")

    if value == "quit".lower():
        sys.exit("\nExiting the Pomodoro tracker.\n")
    elif value == "":
        set_pomodoro()
    elif value.isdecimal():
        try:
            value = int(value)
        except [ValueError]:
            set_pomodoro()

    # 3. Setting the current time
    time_now = datetime.datetime.now()
    print("\n* Current time: {}".format(time_now))

    # 4. Setting the timedelta, ie. the time in future
    set_time = datetime.timedelta(minutes=value)

    # 5. Finding the difference between the current time and future time
    delta = time_now + set_time
    print("* Finishing at: {}\n".format(delta))

    # 6. Waiting till the current time reaches the future time
    # We finish the set pomodoro if current time equals to future time.
    while True:

        if delta == datetime.datetime.now():
            print("Time up! {} minutes completed!".format(value))
            pomodoro_count += 1
            print("\nPomodoros completed: {}".format(pomodoro_count))
            set_pomodoro()


if __name__ == "__main__":
    set_pomodoro()
