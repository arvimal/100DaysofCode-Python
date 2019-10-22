#!/usr/bin/env python3

# Print the first three multiples of a given number `num`,
# and finally return the third multiple.
def first_three_multiples(num):
    for i in range(1, 4):
        print(num * i)
    return num * i


first_three_multiples(10)
first_three_multiples(15)
