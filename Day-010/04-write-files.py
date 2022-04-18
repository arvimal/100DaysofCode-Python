#!/usr/bin/env python3

# If a file exists and it is opened in write mode (w),
# it will be over-written without any warnings.
# Hence, it's better to check the existence of a file
# before opening it for writing.
# Opening a file which has content in `append` mode will
# not overwrite the data, but rather append to it.

# 1. A simple write
with open("/tmp/new_1.txt", "w") as new:
    new.write("This is a text")

# 2. Check for existence
import os

if os.path.exists("/tmp/new.txt"):
    with open("/tmp/new.txt", "a") as handle:
        handle.write("How are you?")
else:
    try:
        with open("/tmp/new.txt", "x") as handle:
            handle.write("Hello World!")
    except Exception:
        pass
