#!/usr/bin/env python3

import os

# os.path() features a lot of functionalities.

# 1. os.path.basename() prints the end leaf name
print(os.path.basename("/tmp/test.txt"))

# 2. os.path.dirname() prints the directory part
print(os.path.dirname("/tmp/test.txt"))

# 3. os.path.exists() check for the existence of paths
print("Checking /tmp/test.txt exists: {}".format(os.path.exists("/tmp/test.txt")))

# 4. os.path.isdir() and os.path.isfile()
if os.path.isdir("/tmp/test.txt"):
    print("/tmp/test.txt is not a folder")
elif os.path.isfile("/tmp/test.txt"):
    print("/tmp/test.txt is a file")

# 5. os.path.join() joins two paths
# It adds `/` if it's Unix, and `\`
# if it's Windows versions
# NOTE: This doesn't check if the path exists.
print(os.path.join("/tmp", "test.txt"))

# 6. os.path.split() splits a path to a dir and file
print(os.path.split("/tmp/test.txt"))
