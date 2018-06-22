#!/usr/bin/env python3

import collections

a = {'a': "A", 'b' : "B"}
b = {'c' : "C", "d" : "D"}

chained_dicts = collections.ChainMap(a, b)

print("Calling individual values from {}".format(chained_dicts))

print("\nKeys: ")
for key in chained_dicts.keys():
    print(key)

print("\nValues")
for val in chained_dicts.values():
    print(val)

print("\nKey and Values")
for key, val in chained_dicts.items():
    print("{} = {}".format(key, val))