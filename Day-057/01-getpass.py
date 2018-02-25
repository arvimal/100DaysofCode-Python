#!/usr/bin/env python3

import getpass
import sys

if sys.stdin.isatty():
    passwd = getpass.getpass("Enter your password: ")
else:
    print("Using readline")
    passwd = sys.stdin.readline().rstrip()

print("Your password: {}".format(passwd))
