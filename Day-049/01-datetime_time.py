#!/usr/bin/env python3

# The `datetime` module includes functions/classes for
# parsing date/time, and overall manipulating it.

import datetime

# Dates are manipulated using the `date` class in `datetime` module.
# whereas time is manipulated using the `time` class in the module.

today = datetime.date.today()

print("Day          : {}".format(today.day))
print("Month        : {}".format(today.month))
print("Year         : {}".format(today.year))
print("Today        : {}".format(today.today()))

print("Min time     : {}".format(datetime.date.min))
print("Max time     : {}".format(datetime.date.max))
print("Resolution   : {}".format(datetime.date.resolution))
