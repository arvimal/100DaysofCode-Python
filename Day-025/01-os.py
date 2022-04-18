#!/usr/bin/env python3

# Creating, deleting folders/files

import contextlib
import os

FOLDER = "/tmp/dir_1"
FILE = "testing.txt"
PATH = FOLDER + FILE

# Checking for pre-existence, and deleting
with contextlib.suppress(OSError):
    os.removedirs(FOLDER)
print(f"Creating {FOLDER}")
os.makedirs(FOLDER)

print(f"Creating `{FILE}` in `{FOLDER}`")

print("Writing content to", FILE)
with open(PATH, "w") as fd:
    fd.write("Hello, How are you?")

print(f"Deleting {FOLDER} and {FILE}")
os.unlink(PATH)
os.removedirs(FOLDER)
