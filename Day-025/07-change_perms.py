#!/usr/bin/env python3

import os
import stat

FOLDER = "/tmp/"
FILE = "testing.txt"
FILE_PATH = FOLDER + FILE

# Removing the file at the start, to
# avoid errors while creating it.
if os.path.exists(FILE_PATH):
    os.unlink(FILE_PATH)

with open(FILE_PATH, "w") as fd:
    fd.write("Hello World!")

current_perms = stat.S_IMODE(os.stat(FILE_PATH).st_mode)
print("Current permissions: {}".format(current_perms))
if not os.access(FILE_PATH, os.X_OK):
    print("No execute permissions for {}".format(FILE_PATH))
    print("Adding execute permissions.")
    new_perms = current_perms | stat.S_IXUSR

os.chmod(FILE_PATH, new_perms)
print("New permissions: {}".format(new_perms))