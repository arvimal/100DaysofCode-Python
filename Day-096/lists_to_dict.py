#!/usr/bin/env python3

"""
Create a dictionary from the two lists below,
the keys being elements from the `drinks` list and
values being elements from the `caffeine` list.
"""

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

output_dict = {key:value for key, value in zip(drinks, caffeine)}

print("\nItems and prices:-\n")
for key in output_dict:
    print("{:<10}: {:<10}".format(key, output_dict[key]))