#!/usr/bin/env python3

# sys.exit() can be used to exit a program midway.
# sys.exit() can take a message and print it while
# exiting.
# sys.exit() can also take a return value, as in the second
# example.

# A crappy example ... :)

import sys

num = int(input("Input a number less than 10: "))
if num > 10 and num < 15:
    # 1. Exit with a message:
    sys.exit("Sorry, try again, Exiting!")
elif num > 15:
    exit_code = 15
    sys.exit(exit_code)
elif num <= 10:
    print("Great")
    sys.exit(0)
