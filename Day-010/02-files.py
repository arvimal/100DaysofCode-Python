#!/usr/bin/env python3

# The python builtin open() is to open a file for read or write.
# open() creates a file descriptor in memory, and the data
# is sent over to this fd.

# 1. Open a file /tmp/new.txt
# NOTE: By default, a file is opened as read-only,
# and only if it exist. This example will hit IOError.
try:
    handle = open("/tmp/new.txt")
except IOError:
    print("No such file or directory.")
finally:
    print("Closing off {0}".format(handle.name))
    handle.close()
    if handle.closed:
        print("File closed")


# 2. Create a file and open it for writing.
# Note: This will error out if the file exists,
# hence we wrap it in a try/except statement.
try:
    f1 = open("/tmp/new.txt", "x")
except FileExistsError: # In Python 3.6
    print("{0} exists!".format(f1.name))
finally:
    f1.close()

