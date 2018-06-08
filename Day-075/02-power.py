#!/usr/bin/env python3

def power(n, power):
    """Prints the power"""

    value = n ** power
    print("%s to the power of %s is %s" % (n, power, value))
    return n, power, value
