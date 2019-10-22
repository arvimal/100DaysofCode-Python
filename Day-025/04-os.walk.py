#!/usr/bin/env python3

# os.walk() generates a tuple containing
# 1. The main directory path
# 2. Immediate sub-dirs of the path
# 3. Files within the sub-dirs

import os
import sys

if len(sys.argv) == 1:
    print(sys.argv[0])
    path = "/tmp"
else:
    path = sys.argv[1]


for dirs, sub_dirs, files in os.walk(path):
    # Print the directories under `path`
    print(dirs)

    # Print the sub-dirs under `path`
    file_path = sub_dirs + files
    # file_path.sort()

    for i in file_path:
        print("\tFiles: {}".format(i))
    print()
