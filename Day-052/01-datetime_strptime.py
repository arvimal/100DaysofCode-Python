#!/usr/bin/env python3

import datetime

time_format = "%a %b %d %H:%M:%S %Y"

today = datetime.datetime.today()
day = datetime.datetime.strptime(today.strftime(time_format), time_format)

print("Today: \n")
print("ISO format: {}".format(datetime.datetime.today()))
print("strftime  : {}".format(today.strftime(time_format)))

print("strptime  : {}".format(day.strftime(time_format)))
