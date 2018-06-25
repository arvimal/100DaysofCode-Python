#!/usr/bin/env python3

import re


def check_name(name=None):
    course_name = re.compile("^([ce]){3}-([a-z]{2})-(\d{3,6})$", re.I)
    name = name.lower()
    if course_name.search(name):
        print("Name formatting correct!")
    else:
        print("Name formatting not correct, try again.")

check_name("cee-an-110")
check_name("cfd-asds-121213")



