#!/usr/bin/env python3

import os

print("Creating a new Environment variable `TESTVAR`")
print(f'Initial value: {os.environ.get("TESTVAR", None)}')

print("Setting `TESTVAR` = `100`")
os.environ["TESTVAR"] = "100"
print(f'New value of `TESTVAR`: {os.environ.get("TESTVAR")}')

print("\nDeleting TESTVAR env variable")
del os.environ["TESTVAR"]
print(f'Current value of `TESTVAR`: {os.environ.get("TESTVAR")}')
