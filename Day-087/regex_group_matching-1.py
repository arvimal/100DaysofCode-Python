#!/usr/bin/env python3

import re


def group_match(num=None):
    if num is None:
        print("The function `group_match` takes a number.")
    else:
        group_num_re = re.compile("(\d\d\d)-(\d\d\d)-(\d\d\d\d)")
        num_search = group_num_re.search(num)

        try:
            if num_search.group():
                print("Your number {} matches the pattern.".format(
                    num_search.group()))
        except AttributeError:
            print("Your number {} does not match the pattern.".format(num))


group_match("123-456-7890")
group_match("1234567890")
group_match("2345-54354-65w56")
group_match("325-654-6546")
