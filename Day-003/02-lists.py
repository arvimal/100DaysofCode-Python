#!/usr/bin/env python3

# Lists

# Create a list
list_1 = []  # Creates an empty list using parantheses
list_2 = list()  # Creates an empty list using the list() builtin

# Lists can accomodate different/multiple data types
list_2 = [1, 2, 3]
list_3 = ["a", "b", "c"]
list_4 = ["a", "hello", 1, "5"]

# Lists can accomodate other lists
list_5 = [[1, 2, 3], [5, 6, 1]]

# Combine a list with an existing list
list_6 = list_5.__add__(list_4)  # Or list_5 + list_4
print(list_6)

print(dir())

# Create a copy of a list
#
# 1. Use `=`
# This is an exact copy, which means any change in one goes in the other
# The new list name is just a reference to the same memory address
list_copy_1 = list_4
print(id(list_copy_1))
print(id(list_4))
list_copy_1 is list_4
#
# 2. Add the elements, rather than assigning the list directly
list_copy_2 = list_4[:]
print(id(list_copy_1))
print(id(list_4))
list_copy_1 is list_4
