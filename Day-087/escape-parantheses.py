#!/usr/bin/env python3

import re


def group_match(num=None):
    if num is None:
        print("The function `group_match` takes a number.")
    else:
        # group_num_re = re.compile("(\d\d\d)-(\d\d\d)-(\d\d\d\d)")
        group_num_re = re.compile("(\(\d\d\))-((\d\d\d)-(\d\d\d)-(\d\d\d))")
        num_search = group_num_re.search(num)

        try:
            if num_search.group():
                print("\n-Your number {} matches the pattern.".format(
                    num_search.group()))
                num_groups = len(num_search.groups())
                print(
                    "  * Number of groups/sections in the number: {}".format(num_groups))
                print("  * Groups: ")
                # print(num_search.groups())
                # print(num_search.groups()[2:])
                print("    1. {}".format(
                    num_search.groups()[0].rstrip(")").lstrip("(")))
                for i in range(len(num_search.groups()[2:])):
                    print("    {}. {}".format(
                        i + 2, num_search.groups()[2:][i]))

        except AttributeError:
            print("\n-Your number {} does not match the pattern.".format(num))


group_match("(91)-986-015-2544")
group_match("9860152544")
group_match("(81)-123-456-7890")
group_match("1234567890")
group_match("(70)-2345-54354-65w56")
group_match("325-654-6546")
