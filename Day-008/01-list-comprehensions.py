#!/usr/bin/env python3

# List comprehensions
# These are hard to understand at first, but seems
# a good knowledge to have. I like them already :)

# NOTE: List comprehensions work on lists and return lists

# Example 1
# Print the elements in list `a`.
a = [1, 2, 3, 4]
b = [i for i in a]
print(b)

# Example 2
# Print the odd elements (0 included) between
# 0 and 11
c = [i for i in range(0, 11, 2)]
print(c)

d = [i for i in range(0, 11, 2) if i % 2 == 0]
print(d[1:])

# Example 3
# Convert a list of ints to strings
e = [10, 20, 30, 40, 50]
f = [str(i) for i in e]
print(f)

# Convert the list `f` back to ints
g = [int(i) for i in f]
print(g)

# Example 4
# String a list of strings from white spaces
h = [" Hello ", "how", "are  ", "you"]
print(h)
print([i.strip() for i in h])

# Example 5
# From the official Python 3 docs
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = [elem for group in vec for elem in group]
print(x)  # Prints all the elements as a single list

y = [elem ** 2 for group in vec for elem in group if elem % 2 == 0]
print(y)  # Prints the squares of odd elemts in vec
