#!/usr/bin/env python3
"""
Recursion is the process of calling the
same function over and over, ie. a loop
without end.

This, will lead to memory overflow, and crash the
interpreter. In order to avoid this, the python
interpreter has a recursion limit inbuilt.

This can be set and fetched using
`sys.getrecursionlimit()` and `sys.setrecursionlimit()`
"""

import sys

print("The current recursion limit: {}".format(sys.getrecursionlimit()))

print("Setting a new recursion limit to 10")
sys.setrecursionlimit(10)

print("The new recursion limit: {}".format(sys.getrecursionlimit()))

print("\nTrying to hit the recursion limit")


def force_recursion(i):
    print("Recursion - level {}".format(i))
    force_recursion(i + 1)


# This should hit a `RecursionError` exception,
# after 10 iterations.
force_recursion(1)
