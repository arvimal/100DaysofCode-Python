#!/usr/bin/env python3


def factorial(x):

    factorial_val = 1

    while x > 1:
        factorial_val *= x
        x -= 1
    print(factorial_val)


factorial(5)
