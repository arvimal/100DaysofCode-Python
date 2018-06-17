#!/usr/bin/env python3

"""
Read an integer `N` and without using any string methods, try to print the following:

1234 .... N (without any spaces in between)

Note that "...." represents the values in between.

* Input Format:

5

* Output Format:

12345
"""


def new_val():
    n = int(input("Enter an integer: "))
    my_list = list(range(1, n + 1))
    print("".join(map(str, my_list)))


new_val()
