#!/usr/bin/env python3

import os

# __file__ can represent the code file that's
# being run, hence we use it here to showcase
# a few features of os.access()

# os.access() tests the access to a file using
# the real uid/gid of the user executing the file

print(f"Calling {__file__}")
print(f"Does exist: {os.access(__file__, os.F_OK)}")
print(f"Is readable: {os.access(__file__, os.R_OK)}")
print(f"Is writable: {os.access(__file__, os.W_OK)}")
print(f"Is executable: {os.access(__file__, os.EX_OK)}")
