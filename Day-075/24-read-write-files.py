#!/usr/bin/env python3

# Reading and writing to files.

# 1. Use the `open` builtin to create a file handler
# `readlines` is used to read all the lines in the file.
# `readlines` returns a list.
# Make sure the file descriptor is closed after the operations.
try:
    fd1 = open("/tmp/new.txt")
    data = fd1.readlines()
    print(data)
    fd1.close()
except IOError:
    print("IOError while reading {0}".format(fd1.name))

# 2. Modes of access
# `open()` takes multiple modes, ie. read, write, read_write etc.
# Refer `help(open)` for details.
"""
Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
"""
try:
    fd2 = open("/tmp/new.txt", "a")
    fd2.write("Hello, I am testing writes!\n")
    fd2.close()
except IOError:
    print("IOError while reading {0}".format(fd2.name))

# 3. Read in various chunks
# Reads can be done as
#   * One line at a time.
#   * Read all lines in a single go (output as a list)
#   * Read the file in chunks.
