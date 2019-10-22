#!/usr/bin/env python3

# Calendar dates can be worked with the `date` class in the
# `datetime` module. [datetime.date.<methods>]

# Instances of the `date` class from `datetime`, inherits methods
# such as `day`, `month`, year` etc.

# The `today` class method of `date` in `datetime` module, can return
# the current date.

import datetime
import pprint

today = datetime.date.today()
print("Date     : {}\n".format(today))

time_tuple = today.timetuple()

print("Year     : {}".format(time_tuple.tm_year))
print("Month    : {}".format(time_tuple.tm_mon))
print("Date     : {}".format(time_tuple.tm_mday))
print("Weekday  : {}".format(time_tuple.tm_wday))
print("Yearday  : {}".format(time_tuple.tm_yday))
