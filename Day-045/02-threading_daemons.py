#!/usr/bin/env python3

# Threads, by default, are spawned as regular threads and hence
# the programs only fully exit once all the threads exit. 

# Threads can be spawned as daemons, which runs in the background
# and parallely, without interferring with the main program, but 
# providing support to it. 

# Example of such a background thread can be a spell checker in a 
# file editor, or a heartbeat checker in a distributed system.

# To start a thread as a daemon, pass `daemon=True` while creating it
# or use its `set_daemon()` method set to `True`.

# By default, the main program flow and other threads don't specifically 
# wait for the `daemon` thread to exit, before exiting themselves.
# ie. Other threads and the program itself can exit even if the `daemon` 
# thread is running. This won't always be ideal
# Refer the next example for `join()` to overcome this.

import threading
import logging
import time

def daemon_thread():
    logging.debug("Starting daemon")
    time.sleep(5)
    logging.debug("Stopping daemon")

def non_daemon():
    logging.debug("Starting non-daemon thread")
    time.sleep(5)
    logging.debug("Exiting non-daemon thread")

logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] (%(threadName)-10s) %(message)s",)

process_1 = threading.Thread(name="Daemon thread", target=daemon_thread,
                             daemon=True)
process_2 = threading.Thread(name="Non-Daemon thread", target=non_daemon)

process_1.start()
process_2.start()

