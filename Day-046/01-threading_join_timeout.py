#!/usr/bin/env python3

import threading
import time
import logging

def my_daemon():
    logging.debug("Starting the `my_daemon` thread")
    time.sleep(10)
    logging.debug("Exiting the `my_daemon` thread")

def norm_thread():
    logging.debug("Starting the `normal` thread")
    logging.debug("Exiting the `normal` thread")


logging.basicConfig(level=logging.DEBUG,
                    format="%(threadName)-1s: %(message)s",)

daemon_thread = threading.Thread(name="daemon_thread", target=my_daemon,
                                 daemon=True)
normal_thread = threading.Thread(name="normal_thread", target=norm_thread)

daemon_thread.start()
normal_thread.start()

daemon_thread.join(timeout=2.0)
normal_thread.join()

print("daemon_thread still alive: {}".format(daemon_thread.isAlive()))
