#!/usr/bin/env python3


MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    """Print name is allowed / not allowed to drive based on MIN_DRIVING_AGE"""
    if age >= 18:
        print("{} is allowed to drive".format(name))
    elif age < 18:
        print("{} is not allowed to drive".format(name))
