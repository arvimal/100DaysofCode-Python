#!/usr/bin/env python3

# Remove duplicates from a list and return a new list.


def remove_duplicates(data):
    new_data = []
    for i in data:
        if i not in new_data:
            new_data.append(i)
    print(new_data)
    return new_data


remove_duplicates([1, 2, 1, 2, 1, 3, 4, 5, 4])
