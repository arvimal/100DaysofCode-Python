#!/usr/bin/env python3

import calendar

cal = calendar.Calendar(calendar.SUNDAY)

cal_data = cal.yeardays2calendar(2017, 3)
print("Length : {}".format(len(cal_data)))

top_months = cal_data[0]
print("Length of top_months: {}".format(len(top_months)))

first_month = top_months[0]
print("Length of first_month: {}".format(len(first_month)))

#print("First month")

