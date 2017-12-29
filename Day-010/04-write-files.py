#!/usr/bin/env python3

# If a file exists and it is opened in write mode (w),
# it will be over-written without any warnings.
# Hence, it's better to check the existence of a file
# before opening it for writing.
# Opening a file which has content in `append` mode will
# not overwrite the data, but rather append to it.

# 1. A simple write
new = open("/tmp/new_1.txt", "w")
new.write("This is a text")
new.close()

# 2. Check for existence
import os
if os.path.exists("/tmp/new.txt"):
    handle = open("/tmp/new.txt", "a")
    handle.write("How are you?")
    handle.close()
else:
    try:
        handle = open("/tmp/new.txt", "x")
        handle.write("Hello World!")
        handle.close()
    except:
        pass

