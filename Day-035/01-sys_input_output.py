#!/usr/bin/env python3

# In Unix, programs access three file descriptors
# for taking in inputs, and processing the outputs.
# stdin, stdout, and stderr

# stdin is the file descriptor which takes in input
# stdout is the file descriptor that prints the output
# stderr is the file descriptor that prints the error.

# This example works by piping the content of a textfile
# to the script.
# The script reads the output of the file as its input
# using `sys.stdin.read()` which is set to the variable
# `data`.

# This input (saved in the `data` variable) is then
# written to stdout using `sys.stdout.write(data)`

# NOTE: Call this is as
# cat README.md | python3.6 -u Day-035/01-sys_input_output.py
import sys

print("Reading from stdin")
data = sys.stdin.read()

print("Writing data to stdout")
sys.stdout.write(data)
sys.stdout.flush()

