#!/usr/bin/env python3

import subprocess

# Using the `communicate()` method on `subprocess.Popen()`
# will give you the stdout and stderr as a tuple.

# stdin is of course the input sent into `subprocess.Popen()`

process = subprocess.Popen(["echo", "Hello guys!"],
                           stdout=subprocess.PIPE)
out, error = process.communicate()

print(out.decode('utf-8'))
print(error)
