#!/usr/bin/env python3

import os

# __file__ can represent the code file that's
# being run, hence we use it here to showcase
# a few features of os.access()

# os.access() tests the access to a file using
# the real uid/gid of the user executing the file

print("Calling {}".format(__file__))
print("Does exist: {}".format(os.access(__file__, os.F_OK)))
print("Is readable: {}".format(os.access(__file__, os.R_OK)))
print("Is writable: {}".format(os.access(__file__, os.W_OK)))
print("Is executable: {}".format(os.access(__file__, os.EX_OK)))
