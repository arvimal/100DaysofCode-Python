#!/usr/bin/env python3

import subprocess
import time

# The poll() method of subprocess.Popen() polls
# for the status of the process
process = subprocess.Popen(["sleep", "1"])
while process.poll() is None:
    print("Still working!")
    time.sleep(0.2)

print(f"Exit status: {process.poll()}")
