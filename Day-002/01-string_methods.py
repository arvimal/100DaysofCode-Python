#!/usr/bin/env python3

# String methods

# Since everything is an object in python, a string is one too.
# The interpreter finds the best fit for the input, and creates
# an instance of the respective class, be it str(), int(), float() etc.

# The instance, hence, will have all the methods defined for the class.

string_1 = "This is a string"
print("Printing the available methods!")
print(dir(string_1))

# String methods

# Converting to upper case.
# This does not change the original string, it stays the same.
# Strings are always immutable.
print(string_1.upper())
print("hello".upper())

# Capitalize the string
# The original string remains the same.
print(string_1.capitalize)

print(string_1.isalpha())
