#!/usr/bin/env python3

import datetime


def set_pomodoro(duration=25):
    """
    Set the pomodoro
    """
    time_now = datetime.datetime.now()
    print("\n{}\n".format(time_now.ctime()))

    duration = int(input("Pomodoro in minutes [25m]: "))
    print("\nYou have chose {} minutes.".format(duration))

    work_duration = datetime.timedelta(seconds=duration * 60)
    print(work_duration)


set_pomodoro(duration=15)
