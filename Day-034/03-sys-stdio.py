#!/usr/bin/env python3

# Standard Input, Standard Output, and Standard Error
# 1. stdin -> Input, normally from a console, or from
# from a program via pipe IPC
# 2. stdout -> Output to the console, or to another
# program via a pipe IPC
# 3. stderr -> Error messages, usually set to write to
# the default stdout, or via a pipe to a process like
# rsyslog, ultimately ending up in a log file.

import sys

print("Reading from stdin:,", file=sys.stderr)
data = sys.stdin.read()
