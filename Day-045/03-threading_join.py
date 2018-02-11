#!/usr/bin/env python3

# As per the previous example, the thread started as `daemon`
# will not block the other threads as well as the main program.
# Hence, the main program and other threads will not wait for the 
# daemon thread to exit, before exiting themselves. This may not
# be always good, depending on the requirements.

# The `threading` module thus provides a method named `join()` 
# which blocks the calling thread and the main program, which makes them
# to wait till the thread calling the `join()` method terminates, either 
# normally or through any sort of exception, or perhaps a timeout.

# This example demonstrates how to join daemon threads so that
# a premature exit of other threads won't end the daemon thread as well.
# ie.. `join()` makes the other threads wait until the thread calling `join()`
# exists.

import threading
import logging
import time

def my_daemon():
    logging.debug("Starting the `my_daemon` thread")
    time.sleep(10)
    logging.debug("Exiting the `my_daemon` thread")

def norm_thread():
    logging.debug("Starting the `normal` thread")
    # We are not setting a sleep here since we want to 
    # make sure that this function exits earlier than 
    # the `my_daemon()` function.
    # But since `my_daemon()` is going to be called 
    # with `join()`, the calling thread has to wait 
    # until `my_daemon()` finishes.
    logging.debug("Exiting the `normal` thread")

logging.basicConfig(level=logging.DEBUG,
                    format='%(threadName)-1s: %(message)s',)

daemon_thread = threading.Thread(name="daemon_thread", target=my_daemon, daemon=True)
normal_thread = threading.Thread(name="normal_thread", target=norm_thread)

daemon_thread.start()
normal_thread.start()

daemon_thread.join()
normal_thread.join()

