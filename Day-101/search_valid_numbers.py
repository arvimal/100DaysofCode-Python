#!/usr/bin/env python3

"""
Check for valid numbers in a phone book.
The Phone book data is given as a dictionary.
Print the user name and phone number, if the number is valid.
Else, print `INVALID PHONE NUMBER`.
"""

import re


def num_check(num_dict=None):
    """
    Phone Number Validator
    """
    phone_num_regex = re.compile("\d\d\d\d\d\d\d\d\d\d")

    print("\n* Analysing data set.")
    if len(num_dict) == 0:
        print("Empty data set, try again.")
    else:
        for key in num_dict:
            if phone_num_regex.search(str(num_dict[key])):
                print("{:<10} : {}".format(key, num_dict[key]))
            else:
                print("{:<10} : INVALID PHONE NUMBER".format(key))


phone_num_dict_1 = {
    "test_1": 9834543287,
    "test_2": 5498723450,
    "test_3": 1948734209,
    "test_4": 5609437821
}

phone_num_dict_2 = {
    "test_1": 9834543287,
    "test_2": 5498723450,
    "test_3": 1948734209,
    "test_4": 5609437821,
    "test_5": 1212
}

phone_num_dict_3 = {}

num_check(phone_num_dict_1)
num_check(phone_num_dict_2)
num_check(phone_num_dict_3)
