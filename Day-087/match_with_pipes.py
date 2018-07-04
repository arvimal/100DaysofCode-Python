#!/usr/bin/env python3

import re
import sys


def check_words(string=None):

    """
    Check your input string for specific words
    such as "Britain", "Ireland", "Wales", "Scotland"
    """

    if string is None:
        print("We need a string to work on.")
        sys.exit(-1)
    else:
        # IMPORTANT: DO NOT PUT SPACES IN BETWEEN PIPES
        # ie. DO NOT use re.compile("Britain | Ireland | Wales | Scotland")
        british_isles_regex = re.compile(
            "Britain|Ireland|Wales|Scotland")
        search_output = british_isles_regex.search(string)

        try:
            if search_output.group():
                print("\n - Your input contains {}".format(search_output.group()))
        except AttributeError:
            print("\n - Your input does not match the pattern.")

check_words("I am calling from Ireland")
check_words("I am not here")
