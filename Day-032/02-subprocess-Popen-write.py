#!/usr/bin/env python3

import subprocess

print("Write: ")

process = subprocess.Popen(["cat", "-"],
                           stdin=subprocess.PIPE,)

process.communicate("Stdin: to stdin".encode('utf-8'))
