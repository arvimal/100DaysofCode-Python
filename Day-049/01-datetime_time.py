#!/usr/bin/env python3

# The `datetime` module includes functions/classes for
# parsing date/time, and overall manipulating it.

import datetime

today = datetime.date.today()

print("Day      : {}".format(today.day))
print("Month    : {}".format(today.month))
print("Year     : {}".format(today.year))
print("today    : {}".format(today.today()))
