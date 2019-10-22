#!/usr/bin/env python3

import subprocess

# The calling program cannot capture the stdout and stdin
# of the processes run by subprocess.run()
# ie.. if we execute this file from bash, it cannot capture
# the stdout/stdin, and thus it's lost
# In order capture those, we can use `subprocess.PIPE` and set
# the `stdout` argument to capture it.
#
completed = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE)

print("Return Code: {}".format(completed.returncode))

print("\nstdout : {}".format(completed.stdout.decode("utf-8")))
