#!/usr/bin/env python3

# The `subprocess` module helps to start and
# control processes in an operating system

import subprocess

# The `call()` function/method
# This enables to call binaries/scripts etc.
# This returns a return code, which can be captured
# in a variable
subprocess.call("/usr/bin/terminator")
# The return status is populated once the process terminates
status = subprocess.call("/usr/bin/gedit")
if status == 0:
    print("Process start a success!")
else:
    print("Process start a failure")
print("Return status: {}".format(status))
