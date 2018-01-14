#!/usr/bin/env python3

import os
import stat

FOLDER = "/tmp/"
FILE = "testing.txt"
FILE_PATH = FOLDER + FILE

with open(FILE_PATH, "w") as fd:
    fd.write("Hello World!")

