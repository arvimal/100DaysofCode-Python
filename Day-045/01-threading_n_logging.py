#!/usr/bin/env python3

# The `logging` module supports and can log messages
# from multiple threads within the same process, separately.
# Hence, it's easy to include logs from specific threads.

# In short, the `logging` module is thread-safe, hence messages from
# different threads are kept different in the logs.

import threading
import logging
import time

# Our function which will be called by our threads
def my_worker_func():
    logging.debug("Starting the worker function!")
    time.sleep(5)
    logging.debug("Stopping the worker function!")

logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] (%(threadName)-10s) %(message)s",)

thread_1 = threading.Thread(name="Worker function 1", target=my_worker_func)
thread_2 = threading.Thread(name="Worker function 2", target=my_worker_func)

thread_1.start()
thread_2.start()

