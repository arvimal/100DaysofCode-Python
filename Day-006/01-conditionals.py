#!/usr/bin/env python3

# Conditional statements check for a condition,
# and act accordingly.
# Python uses the `if/elif/else` structure for this.

# Example 1
if 2 > 1:
    print("2 greater than 1")

# Example 2
var1 = 1
var2 = 10
if var1 > var2:
    print("var1 greater than var2")
else:
    print("var2 greater than var1")

# Example 3
# Ask for an input
value = input("What is the price for that thing?")
value = int(value) # Try converting it to an int
if value < 10:
    print("That's great!")
elif 10 <= value <= 20:
    print("I would still buy it!")
else:
    print("That's costly!")

