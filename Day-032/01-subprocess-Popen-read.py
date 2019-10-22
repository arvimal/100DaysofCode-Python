#!/usr/bin/env python3

import subprocess

print("Read: ")

process = subprocess.Popen(["echo", "to stdout"], stdout=subprocess.PIPE)

stdout_value = process.communicate()[0].decode("utf-8")
print("stdout:", repr(stdout_value))
