#!/usr/bin/env python3

# Each thread has a default name assigned to it,
# and this can be fetched by `threading.Thread().name`,
# as seen in the previous day's example.

# The default name can be changed by using the `name` argument
# to `threading.Thread(name=<custom_name>`, target=<function>)`

import threading
import time
import pprint


def my_worker():
    print("Starting {}".format(threading.current_thread().getName()))
    time.sleep(5)
    print("Exiting thread {}".format(threading.current_thread().getName()))


thread_list = []

for i in range(10):
    t = threading.Thread(name="Worker thread", target=my_worker)
    thread_list.append(t)
    t.start()

pprint.pprint(thread_list)
