#!/usr/bin/env python3

# The `sys.getsizeof()` method allows to fetch the
# size of the objects in the namespace.

import sys

print("Getting an object size listing:\n")
for i in dir():
    print("{:>20} : {}".format(i, sys.getsizeof(i)))

##
print("\nCreating new objects.")

# Class
class MyClass:
    pass


# Function
def my_func():
    pass


# Lists:
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

##
print("Getting a new object size listing:\n")
for i in dir():
    print("{:>20} : {}".format(i, sys.getsizeof(i)))
