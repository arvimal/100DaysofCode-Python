#!/usr/bin/env python3

# Sets are unordered collections of unique elements.
# A list with recurring elements when converted to
# a set will only have elements occuring once.

my_list = [1, 2, 1, 3, 4, 5]
print(my_list)

my_set = set(my_list)
print(my_set)

# The set when called from the python REPL, will be
# similar to a list with curly brackets without any
# elements recurring.
"""
In [1]: my_list = [1, 2, 1, 3, 4, 5]

In [2]: my_list
Out[2]: [1, 2, 1, 3, 4, 5]

In [3]: my_set = set(my_list)

In [4]: my_set
Out[4]: {1, 2, 3, 4, 5} #
"""

list_1 = [1, 2, 3, 4, 4, 6, 1, 2, 5]
set_1 = {x for x in list_1}  # Or simply, set(list_1)
print(set_1)
