#!/usr/bin/env python3

import sys


def dec_to_bin(value):
    """
    Converts decimal to binary
    """
    pos_values = (128, 64, 32, 16, 8, 4, 2, 1)
    result = []

    if any([value > 255, value < 0]):
        sys.exit("Value out of range")

    else:
        for element in pos_values:
            if value == element:
                result.append(value)
            return result
            elif value < element:




dec_to_bin(259)
