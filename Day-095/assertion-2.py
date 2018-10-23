#!/usr/bin/env python3

"""
Write an assert statement that triggers an AssertionError
if the variable spam is an integer greater than 10.
"""

def check_int(spam=None):
    """
    IMPORTANT:
    Note that we are asserting (forcing) a condition,
    and the Assert kicks in when the condition is not satisfied.
    Hence, to raise the assert for any numbers greater than 10,
    we have to enforce the number to be less than 10.

    """
    assert int(spam) < 10, "Integer value greater than 10"


for num in range(8, 15):
    print("\nTrying {}\n".format(num))
    check_int(num)

"""
check_int(1)
check_int(10)
check_int(15)
"""