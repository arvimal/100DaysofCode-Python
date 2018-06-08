#!/usr/bin/env python3

import sys


def digit_sum(x):
    """Add the digits in a number `x`"""
    final_val = 0
    if type(x) != int:
        sys.exit("Expecting an integer!")
    num_str = str(x)
    for i in num_str:
        final_val += int(i)
    print(final_val)
    # return final_val


digit_sum(123456789)
