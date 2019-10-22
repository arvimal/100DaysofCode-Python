#!/usr/bin/env python3

# while loops do the looping only until a certain
# condition remains met.

i = 0
while i < 10:
    print(i)
    i += 2

# Checking for a `True` condition using `while`
# will always be running.

# while True:
#   print(">>>")

# break
# `break` is used to break out of a loop, usually a while loop,
# when another condition is met.

while i < 10:
    print(i)
    if i == 5:
        break
    i += 1
