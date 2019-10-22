#!/usr/bin/env python3

# The `Timer` class in `threading` (called threading.Timer())
# calls a function after a delay of N seconds.

# The `Timer` class inherits from the `threading.Thread` class.

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format="[%(threadName)-1s] %(message)s")


def delayed():
    logging.debug("Worker thread running.")


t1 = threading.Timer(0.5, delayed)
t1.setName("thread_1")

t2 = threading.Timer(0.5, delayed)
t2.setName("thread_2")

logging.debug("\nStarting timers")
t1.start()
t2.start()

logging.debug("Sleeping for 5 seconds")
time.sleep(5)

logging.debug("Cancelling {}".format(t2.getName()))
t2.cancel()
