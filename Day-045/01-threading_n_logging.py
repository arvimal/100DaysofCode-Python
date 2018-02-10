#!/usr/bin/env python3

import threading
import logging
import time


def my_worker_func():
    logging.debug("Starting the worker function!")
    time.sleep(5)
    logging.debug("Stopping the worker function!")

logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] (%(threadName)-10s) %(message)s",)

process_1 = threading.Thread(name="Worker function 1", target=my_worker_func)
process_2 = threading.Thread(name="Worker function 2", target=my_worker_func)

process_1.start()
process_2.start()

