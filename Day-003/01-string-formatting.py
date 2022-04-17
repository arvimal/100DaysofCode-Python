#!/usr/bin/env python3

# String formatting helps to put different types
# within a string.

# 1. Old way of string formatting

# Strings
string_1 = "This is a %s" % ("test")
print(string_1)

# Multiple strings
string_2 = "I like %s and %s" % ("bacon", "eggs")
print(string_2)

# Integers
string_3 = "%i + %i = %i" % (1, 2, 3)
print(string_3)

# Floats
string_4 = "%f" % (1.23)
print(string_4)

# Specify the number of places after the decimal
string_5 = "%.2f" % (1.23456)
print(string_5)  # Print just two places

string_6 = "%.4f" % (1.26789)
print(string_6)  # Prints to four places

# Templates in string formatting

# Strings
print("%(food)s is tasty" % {"food": "Bacon"})
print("%(value)s, %(value)s, %(value)s" % {"value": "SPAM"})

# Integers
print("%(a)i + %(b)i + %(c)i = %(d)i" % {"a": 1, "b": 2, "c": 3, "d": 7})

# 2. A more sane method, using format()

# Formatting using Positional arguments
print("{0} is {1}".format("Bacon", "Awesome"))
print("{0} + {1} = {2}".format(1, 2, 3))
print("{0} + {1} = {3}".format(1, 2, 1, 3))
print("{0}, {1}, {2}".format("a", "b", "c"))
print("{}, {}, {}".format("a", "b", "c"))
print("{2}, {1}, {0}".format("a", "b", "c"))

# Normal formatting
name = "Sherlock"
print("Hello {}".format(name))

# Unpacking the positional values in a string
print("{4} is the sum of {1} and {3}".format(*"012345"))
print("{1}{0}{1}! You're done!".format("cad", "abra"))

# Aligning text
print("{:30}".format("testing"))  # No effect
print("{:^30}".format("Center aligned"))
print("{:<30}".format("Left aligned"))
print("{:>30}".format("Right aligned"))

# 3. The latest, using `f-strings`
print("This is F-Strings")
print(f"My name is {name}")
