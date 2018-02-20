#!/usr/bin/env python3

# Lambda example 1

import math

# Normal Function


def sqroot(x):
    return math.sqrt(x)


# Lambda Function
square_root = lambda x: math.sqrt(x)


# Calling the functions
print(sqroot(16))
print(square_root(16))
