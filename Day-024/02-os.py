#!/usr/bin/env python3

# We have seen os.chdir(), os.getcwd()
# in a previous example.

# os.pardir moves to the parent directory

import os

os.rmdir("/tmp/test_1")
os.mkdir("/tmp/test_1")
os.chdir("/tmp/test_1")
print(os.getcwd())
os.chdir(os.pardir)
print(os.getcwd())