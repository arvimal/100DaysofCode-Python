#!/usr/bin/env python3

import sys

print("Printing the python interpreter version")
print(sys.version + "\n")

print("Printing the interpreter version in hex")
# Converting sys.hexversion into string to add to "\n"
# since it's an int by default, and `+` will error out
print(str(sys.hexversion) + "\n")

print("Printing the interpreter version in a tuple")
print(sys.version_info)

print("\n`sys.version_info` can be used for checking\
 python versions in programs")
print("Interpreter information:")
print("Major version: {0:5}".format(sys.version_info[0]))
print("Minor version: {0:5}".format(sys.version_info[1]))

print("\nOther information:")
print("C API version: {0:5}".format(sys.api_version))
print("Platform: {0:10}".format(sys.platform))

print(sys.implementation)