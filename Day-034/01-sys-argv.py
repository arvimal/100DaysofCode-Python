#!/usr/bin/env python3

"""
The `sys` module provides system specific operations
and configurations.

It also provides options to interact with the configuration
of the interpreter at runtime, and configurations outside
the running program.
"""

# `sys.argv` prints all the arguments as a list
import sys

# 1. Print all the args as a list.
# If no args are present, print argv[0]
print(sys.argv)

# 2. Print the first argument, ie. the program name
print(sys.argv[0])

# Running this program with multiple arguments
# from the terminal, will print all the arguments
# to stdout
# For example:
# python3.6 01-sys-argv.py -v test
# ['01-sys-argv.py', '-v', 'test']

if __name__ == "__main__":
    print(sys.argv)
