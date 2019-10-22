#!/usr/bin/env python3

# Loops are to iterate through data,
# and is done through an iterable.

# Python have two loop constructs, the `for` and `while` loop

# A for loop creates an iterable and reads the
# value that is assigned to it, and performs the
# required actions.

for i in [1, 2, 3, 4]:
    print(i)

# The range() builtin function does the same,
# but returns a list.
print(range(1, 10))

# Looping over a dict
my_dict = {"a": 1, "b": 2, "c": 3}
for i in my_dict.keys():
    print(i)

# Another example:
for num in range(10):
    if num % 2 == 0:
        print(num)
