#!/usr/bin/env python3

# A normal `open()` will open a new file descriptor,
# and it has to be closed manually, else it can end up
# showing unexpected data.

# A `with` statement does not require you to close the fd
# but will close it automatically when the reference is done with.

# The file handler will be closed once the code block is finished
# Hence, all fd operations has to be done within the code block.
with open("/tmp/new.txt") as handle:
    content = handle.readlines()
    print(content)

# Catching errors, while using `with`.
try:
    with open("/tmp/new.txt") as file_handler:
        for line in file_handler:
            print(line)
except IOError:
    print("IOError")

