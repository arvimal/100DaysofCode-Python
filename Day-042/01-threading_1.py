#!/usr/bin/env python3

import threading
import pprint

# Define a function which we want to run via threads.


def worker():
    print("Thread: ")


thread_list = []
# Calling `threading.Thread()` in a loop so that
# the function `worker` can be called multiple times,
# all of them through threads.
for i in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)
    thread.start()

# Print the thread_list list to understand what the threads were.
pprint.pprint(thread_list)
