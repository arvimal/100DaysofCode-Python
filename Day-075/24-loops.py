#!/usr/bin/env python3

# Python has two types of loops, `for` and `while`.

# 1. `for loops
print("Example 1 : for loops")
for i in [1, 2, 3, 4, 5]:
    print(i)

# 2. `while` loop
# NOTE: `while` loops can end up in infinite loops
# if there no start and end conditions such as `j=0`
# and `j <= 5`.
print("Example 2 : while loop")
j = 0
while j <= 5:
    print("Good morning!")
    j += 1

print("Example 3 : while loop")
d = 0
while d < 10:
    print(d)
    if d == 5:
        break
    d += 1
# 3. range()
# range() is a builtin function that gives a stretch of elements
# which ideally can be iterated over using a `for` loop
print("Example 4 : range()")
print(range(5))

# This prints the power of the numbers between 1 and 10
# skipping one number in between
print("Example 5 : for loop and range()")
for b in range(1, 11, 2):
    print(b ** 2)

# This can be also shortened via list comprehensions
print("Example 6 : Iterating over a range() with list comprehensions")
print([b ** 2 for b in range(1, 11, 2)])
