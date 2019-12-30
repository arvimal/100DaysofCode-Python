#!/usr/bin/env python3

# HackerRank Problem
# https://www.hackerrank.com/challenges/write-a-function/problem

# Source: Wikipedia - https://en.wikipedia.org/wiki/Leap_year
# The following pseudocode determines whether a year is a leap year or a common year
# in the Gregorian calendar (and in the proleptic Gregorian calendar before 1582).
# The year variable being tested is the integer representing the number of the year
# in the Gregorian calendar.

# if (year is not divisible by 4) then(it is a common year)
# else if (year is not divisible by 100) then(it is a leap year)
# else if (year is not divisible by 400) then(it is a common year)
# else (it is a leap year)


def is_leap(year):
    leap = False
    if year % 4 != 0:
        pass
    elif year % 100 != 0:
        leap = True
    elif year % 400 != 0:
        leap = False
    else:
        leap = True
    print(leap)
    return leap

is_leap(2000)
