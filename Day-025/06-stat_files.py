#!/usr/bin/env python3

"""
os.stat() and os.lstat() can give detailed info
about a file/folder, similar to a `stat` in Linux.
"""

import os
import sys

if len(sys.argv) == 1:
    # Set path to /tmp for our work
    # if path is not provided as an argument.
    path = "/tmp"
else:
    # if a path is provided as an argument to this script,
    # set path to sys.arg[1]
    path = sys.argv[1]

info = os.stat(path)

print("Stating {}".format(path))
print("Name      : {}".format(path))
print("UID       : {}".format(info.st_uid))
print("GID       : {}".format(info.st_gid))
print("Created on: {}".format(info.st_ctime))

print("\nStating all info")
print(info)
