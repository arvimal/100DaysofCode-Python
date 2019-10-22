#!/usr/bin/env python3


def search_unordered_list(number_list):
    """
    Search a given list for the largest number
    """

    largest_number = 0

    for num in number_list:
        if num > largest_number:
            largest_number = num
        else:
            pass
    print(
        "{} at position {} is the largest number".format(
            largest_number, number_list.index(largest_number) + 1
        )
    )
    return largest_number


number_list = [100, 120, 1, 10, 5, 988, 2, 666, 32, 90, 23]
search_unordered_list(number_list)
