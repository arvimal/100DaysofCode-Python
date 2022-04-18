#!/usr/bin/env python3

# Sets are denoted with curly brackets {}
# They are similar to lists
# (1) Mutable
# (2) Hold any data type.
#
# The differences are:
# (1)   Lists can carry the same element multiple times
#       Sets cannot have duplicate elements.
# (2)   Lists are ordered
#       Sets are un-ordered
# (3)   Searching a set is faster compared to a list,
#       due to hashing like a dict
#
# Typical use-case of a set is to omit duplicates, find intersections/common, etc


# Create sets
set1 = set()  # <== Creates an empty set
set2 = {}  # <== Common mistake. This creates an empty dict

set3 = {1, 2, 3, 4, 5}  # <== Creates a set with elements
set4 = {1, 2, 3, 4, 5, 4, 4, 2, 3, 4}  # <== Creates a set but omit duplicates

# Print type
for elem in set1, set2, set3, set4:
    print(f"{str(elem)} is of type {type(elem)}")

##
# Changing a list (that has multiple similar elements) to a set, will
# remove the duplicates

lst_1 = [12, 12, 13, 14, 14, 14, 15, 200, 200]
set_1 = set(lst_1)  # <== set_1 is created from lst_1
print(set_1)
