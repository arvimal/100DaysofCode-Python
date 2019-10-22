#!/usr/bin/env python3

# This example showcases the `timeout` feature for the
# join() method.

# We mentioned in the example prior, that the `join()` method
# blocks the calling thread until the thread that calls the `join()`
# method terminates.

# The `timeout` argument for the `join()` method takes in a float,
# ie. the number of seconds the join() method will stay/timeout in.

# In this example, we are forcing the `my_daemon` thread to sleep for
# 10 seconds, as the previous examples.
# Both the threads are spawned by `threading.Thread()` and `join()` is
# called on both of them, so that they will wait till the sleeping
# thread exits on its own.

# But since we passed a lower timeout value through `join()` for
# daemon_thread`, the join() method is not enforced anymore, and hence
# other threads can finish without waiting for `daemon_thread` to exit.

# Because of the timeout value in `join()` and a larger sleep value for
# `daemon_thread`, the `daemon_thread` is still alive when `normal_thread`
# exits.

# This can be verified through the `isAlive()` method for the thread.
# This shows that the daemon_thread is still alive while all other threads
# have exited.

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


logging.basicConfig(level=logging.DEBUG, format="%(threadName)-1s: %(message)s")

daemon_thread = threading.Thread(name="daemon_thread", target=my_daemon, daemon=True)
normal_thread = threading.Thread(name="normal_thread", target=norm_thread)

daemon_thread.start()
normal_thread.start()

daemon_thread.join(timeout=2.0)
normal_thread.join()

print("\nnormal_thread still alive: {}".format(normal_thread.isAlive()))
print("daemon_thread still alive: {}".format(daemon_thread.isAlive()))
