#!/usr/bin/env python3

import os

print("Creating a new Environment variable `TESTVAR`")
print("Initial value: {}".format(os.environ.get("TESTVAR", None)))

print("Setting `TESTVAR` = `100`")
os.environ["TESTVAR"] = "100"
print("New value of `TESTVAR`: {}".format(os.environ.get("TESTVAR")))

print("\nDeleting TESTVAR env variable")
del os.environ["TESTVAR"]
print("Current value of `TESTVAR`: {}".format(os.environ.get("TESTVAR")))