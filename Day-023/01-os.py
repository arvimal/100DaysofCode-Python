#!/usr/bin/env python3

import os

print("Checking if /tmp/folder_1 exists, deleting!")
try:
    os.rmdir("/tmp/folder_1")
except OSError:
    pass
print("Changing to /tmp/")
os.chdir("/tmp")
print("Creating folder_1")
os.mkdir("folder_1")
print("Deleting /tmp/folder_1")
os.rmdir("/tmp/folder_1")

print("\nRename a folder using os.rename()")
print("Creating /tmp/dir_1")
os.mkdir("/tmp/dir_1")
print("Checking if the rename worked or not")
try:
    os.rename("/tmp/dir_1", "/tmp/dir_2")
except:
    print("Rename failed.")
print("os.renames() helps to rename dirs and files recursively")
print("/tmp/dir_1 exists: {}".format(os.path.exists("/tmp/dir_1")))
print("/tmp/dir_2 exists: {}".format(os.path.exists("/tmp/dir_2")))

# os.walk walks through a directory,
# and can find all the sub-dirs and files within
for root, dirs, files in os.walk("/tmp/"):
    print("{} : {} / {}".format(root, dirs, files))
