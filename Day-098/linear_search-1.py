#!/usr/bin/env python3

"""
Create a linear search function,
that searches a list for a specific value
"""

def linear_search(search_list, search_value):
    print("Starting linear search for {}".format(search_value))

    for val in search_list:
        if val is search_value:
            print("\n{} found at position {}.\n".format(val, search_list.index(val) + 1))
        else:
            print("{} not found in the data set".format(search_value))

linear_search([1, 10, 33, 13, 14, 65, 43], 43)
linear_search([1, 10, 33, 13, 14, 65, 43], 65)
linear_search([1, 10, 33, 13, 14, 65, 43], 12)


