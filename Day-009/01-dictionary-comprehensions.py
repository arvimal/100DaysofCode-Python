#!/usr/bin/env python3

# Dictionary comprehensions originated in Python v3,
# but were backported to v2.

# Example 1
# This creates a key and value from a range
print({i: str(i) for i in range(5)})
# {0: '0', 1: '1', 2: '2', 3: '3', 4: '4'}

# Example 2
# Swap the key and value pairs in a dict
dict_1 = {0: "Hello", 1: "World!"}
print({value: key for key, value in dict_1.items()})
