#!/usr/bin/env python3

import time

print("Date/Time now {}".format(time.ctime()))
print("Seconds from EPOCH : {}".format(time.time()))
print("Sleeping 5 seconds")
time.sleep(5)
print("Date/Time now {}".format(time.ctime()))
print("Seconds from EPOCH : {}".format(time.time()))
