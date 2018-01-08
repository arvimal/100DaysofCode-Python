#!/usr/bin/env python3

import logging

LOG_FILE = "log_file.log"

logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)

logging.DEBUG("DEBUG: This will be logged")

with open(LOG_FILE, "r") as fd:
    data = fd.read()

print(data)
