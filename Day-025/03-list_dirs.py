#!/usr/bin/env python3

import os
import sys

# List the contents in a folder using os.listdir()

# 1. An example to list the content in a dir passed as an
# argument
print(os.listdir(sys.argv[1]))
print("\n")

# 1. List contents in /tmp
print(os.listdir("/home"))
