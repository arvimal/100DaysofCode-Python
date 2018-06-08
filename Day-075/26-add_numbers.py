#!/usr/bin/env python3

"""
Write a function that can sum up numbers. It should receive a list of n numbers.
If no argument is provided, return sum of numbers 1..100.
"""


def sum_numbers(numbers=None):
    if numbers is None:
        sum_of_num = 0
        for i in range(1, 101):
            sum_of_num += i
        return sum_of_num
    else:
        sum_of_num = 0
        for i in range(len(numbers)):
            sum_of_num += numbers[i]
        return sum_of_num


print(sum_numbers(numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
