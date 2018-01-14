#!/usr/bin/env python3

# os.scandir() returns an iterator
# This iterator stands for a directory-entry for
# the folder passed to `os.scandir(<folder>).
# This iterator also gives methods which can be used
# to check if the entry is a file, folder, symlink etc.
# The iterator can be stat using <iterator>.stat

import os
import sys

if len(sys.argv) == 1:
    path = "/tmp"
else:
    path = sys.argv[1]

for i in os.scandir(path):
    if i.is_dir():
        data_type = "Directory"
    elif i.is_file():
        data_type = "File"
    elif i.is_symlink():
        data_type = "Symbolic link"
    print("\n# `{}`".format(i.name))
    print("\tType: {}".format(data_type))
    print("\tInode #: {}".format(i.stat().st_ino))
    print("\tModified time: {}".format(i.stat().st_mtime))

    print("\tStating all info: \n{}".format(i.stat()))