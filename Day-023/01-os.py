#!/usr/bin/env python3

import contextlib
import os

# Read more on the contextlib module, it's very powerful!
print("Checking if /tmp/folder_1 exists, deleting!")
with contextlib.suppress(OSError):
    os.rmdir("/tmp/folder_1")
#
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
except Exception:
    print("Rename failed.")
print("os.renames() helps to rename dirs and files recursively")
print(f'/tmp/dir_1 exists: {os.path.exists("/tmp/dir_1")}')
print(f'/tmp/dir_2 exists: {os.path.exists("/tmp/dir_2")}')

# os.walk walks through a directory,
# and can find all the sub-dirs and files within
for root, dirs, files in os.walk("/tmp/"):
    print(f"{root} : {dirs} / {files}")
