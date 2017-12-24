#!/usr/bin/env python3

# A Dictionary is a hash table or hash mapping.
# In other languages, they may be referred to as
# Associative Arrays or Associative Memories

# A dict is indexed with keys, which can be any immutable type.

# Dicts are Unordered while returning, but 3.6.1(?) promises
# dicts would be sorted while returning.

# 1. Creating dicts
first_dict = {}
second_dict = dict()
third_dict = {"one": 1, "two": 2, "three": 3}

# Note:
# Printing multiple dicts returns a tuple.
# Printing a single dict returns a dict.
print(first_dict, second_dict, third_dict)
print(third_dict)

# Access values in dicts
# Values are accessed using keys
print(third_dict["one"])
# List all keys in a dict
print(third_dict.keys())
