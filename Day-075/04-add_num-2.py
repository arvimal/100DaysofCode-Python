#!/usr/bin/env python3


def sum_digits(x):
    print(sum(int(i) for i in str(x)))
    return sum(int(i) for i in str(x))


sum_digits(123456789)
sum_digits(12)
