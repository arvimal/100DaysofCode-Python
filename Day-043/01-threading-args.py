#!/usr/bin/env python3

# The `threading.Thread()` takes a target as well as arguments,
# that can be then processed.

import threading
import pprint
import time


def worker(text):
    print("I am a function being called by a worker thread: {}".format(text))


threads = []

for num in range(10):
    # Creating the thread by calling `threading.Thread()`
    # on the required function that has to be threaded.
    t = threading.Thread(target=worker, args=(num + 1,))
    # Appending the thread info to the list
    threads.append(t)
    t.start()
    print("Starting thread # {}: {}".format(num + 1, t))
    print(t.name)


pprint.pprint(threads)
