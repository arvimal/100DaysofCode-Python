#!/usr/bin/env python3


def is_int(x):
    # real = x // 1
    deci = x % 1
    if deci == 0.0:
        print("An int")
    elif deci != 0.0:
        print("A float")


def is_int(x):
    import math

    real, deci = math.modf(x)
    if deci == 0.0:
        print("An int")
    elif deci != 0.0:
        print("A float")
