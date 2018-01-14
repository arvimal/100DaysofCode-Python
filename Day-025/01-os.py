#!/usr/bin/env python3

# Creating, deleting folders/files

import os

FOLDER = "/tmp/dir_1"
FILE = "testing.txt"
PATH = FOLDER + FILE

# Checking for pre-existence, and deleting
os.removedirs(FOLDER)

print("Creating {}".format(FOLDER))
os.makedirs(FOLDER)

print("Creating `{}` in `{}`".format(FILE, FOLDER))

print("Writing content to", FILE)
with open(PATH, "w") as fd:
    fd.write("Hello, How are you?")

print("Deleting {} and {}".format(FOLDER, FILE))
os.unlink(PATH)
os.removedirs(FOLDER)
