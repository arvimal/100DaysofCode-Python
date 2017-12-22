#!/usr/bin/env python3

# Lists

# Create a list
list_1 = [] # Creates an empty list using parantheses
list_2 = list() # Creates an empty list using the list() builtin

# Lists can accomodate different/multiple data types
list_2 = [1, 2, 3]
list_3 = ["a", "b", "c"]
list_4 = ["a", "hello", 1, "5"]

# Lists can accomodate other lists
list_5 = [[1, 2, 3], [5, 6, 1]]

# Combine a list with an existing list
list_6 = list_5.__add__(list_4) # Or list_5 + list_4
print(list_6)

# print(dir())