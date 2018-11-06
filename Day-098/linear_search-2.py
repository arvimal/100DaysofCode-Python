#!/usr/bin/env python3

"""
Create a linear search function,
that searches a list for a specific value
"""

def linear_search(search_list, search_value):
    print("\nStarting linear search for {}\n".format(search_value))

    for num in range(len(search_list)):
        if search_list[num] == search_value:
            print("\n**{} found at position {}.\n".format(
                num,
                search_list.index(num) + 1))
    else:
        print("**{} not found in the data set".format(search_value))

linear_search([1, 10, 33, 13, 14, 65, 43], 43)
linear_search([1, 10, 33, 13, 14, 65, 43], 65)
linear_search([1, 10, 33, 13, 14, 65, 43], 12)


