#!/usr/bin/env python3

# The logging module helps in logging your code.
# We pass a filename, and a logging level.
# There are five levels of logging
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

# The file will be appended with the logs, by default.
# Overwriting the log file is possible with adding
# `filemode="w"`.

# The `basicConfig()` method allows to log to a file,
# else it logs to stdout.

import logging

logging.basicConfig(filename="test.log", level=logging.INFO)
log = logging.getLogger("mylogger")

try:
    raise RuntimeError
except RuntimeError:
    log.exception("RuntimeError hit")
