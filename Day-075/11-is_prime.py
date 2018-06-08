#!/usr/bin/env python3

    """Find if the number is a prime"""
    # 1. Test if the number is evenly divisible by n, n being `2` to `x-1`
    # 2. If divisible, return False and exit, else continue to next number.
    # a. A loop from `2` and `x -1`
    # While using `range`, use `x` as the max end, since it always reduces one.


def is_prime(x):
    """Finding prime numbers"""

    if x in [0, 1]:
        return False
    elif x < 0:
        return False
    elif x == 2:
        return True
    elif x > 2:
        for i in range(2, x):
            if x % i == 0:
                return False
    return True


is_prime(100)
