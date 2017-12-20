#!/usr/bin/env python3

# Strings

# Quotes can be either single, double, or triple.
string_1 = "Day 1 of #100DaysofCode!"
string_2 = 'Day 1 of #100DaysofCode!'
string_3 = """Day 1 of #100DaysofCode!"""
string_4 = '''Day 1 of #100DaysofCode!'''

# If the line contains a single quote,
# escape it with double quotes
string_5 = "Today's Day 1 of #100DaysofCode"
string_6 = 'Today is "Day 1" of #100DaysofCode'

# Convert ints to strings, ie. typecasting
string_7 = 123
string_8 = str(string_7)
print(type(string_8))

# Typecasting strings to ints won't work
string_9 = "test"
print(type(int(string_9)))

# Strings are immutable
# Trying to change an element in a string will fail.
string_10 = "Hello"
string_10[1] = "0"

# ASCII and Unicode
# Python2.x strings can only contain ASCII chars.
# Python3.x strings are all Unicode, and hence support more than ASCII
# The following example doesn't contain unicode, but serves as an example.
unicode_String = u"This is unicode"

# String concatenation
# Strings can be concatenated
string_11 = string_10 + string_9
print(string_11)