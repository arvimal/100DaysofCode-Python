#!/usr/bin/env python3

import logging
logging.basicConfig(filename="test.log", level=logging.INFO)

logging.debug("This is a DEBUG level message")
logging.info("This is an INFO level message")
logging.error("This is an ERROR level message")