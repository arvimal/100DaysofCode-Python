#!/usr/bin/env python3

import os

# os.walk walks through a directory,
# and can find all the sub-dirs and files within
for root, dirs, files in os.walk("/tmp/"):
    print("{} : {} / {}".format(root, dirs, files))

