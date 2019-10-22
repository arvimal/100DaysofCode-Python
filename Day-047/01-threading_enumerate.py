#!/usr/bin/env python3

# The `enumerate()` method returns a list of active `threading.Thread()`
# instances.

# This list will include the current thread, and all other threads.

# NOTE: (From PyMOTW3)
# The current thread should not be joined with `join()`, since
# it will introduce a deadlock with other threads.

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format="(%(threadName)-1s %(message)s")


def my_worker():
    logging.debug("`my_worker` thread started")
    time.sleep(5)
    logging.debug("`my_worker` thread sleeping for 5 seconds")
    logging.debug("`my_worker` thread ending")


for i in range(5):
    thread = threading.Thread(target=my_worker, daemon=True)
    thread.start()

main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug("Joining %s", t.getName())
    t.join()
