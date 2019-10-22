#!/usr/bin/env python3

import subprocess

# This runs the `false` command on the terminal, and it
# always return a return status of `1`.
# A normal execution of this command does not print the
# error to stderror, as the example below.
# Using run() without passing check=True is equivalent
# to using call(), and it only returns the exit code.
subprocess.run(["false"])

# But if the argument `check=True` is used, the return code
# is checked, and if it is an error, a `CalledProcessError`
# exception is raised onto stdout.
# The following example, shows that.
# subprocess.run(["false"], check=True)

# The following example uses the `check=True` but tries
# to handle the expected `CalledProcessError`.

# NOTE: Comment the above example, to get the below example
# executed. If not, you won't get the below one executed
# since the above one is designed to hit an exception and
# hence won't proceed further down.
try:
    subprocess.run(["false"], check=True)
except subprocess.CalledProcessError as e:
    print("Exception hit")
    print(e)
