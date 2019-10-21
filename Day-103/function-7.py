#!/usr/bin/env python3

# Remainders in division

# Should take two values, and return the remainder of twice first arg 
# divided by the half of second arg.

def remainder(num1, num2):
  return ((num1 * 2) % (num2 / 2)) 


print(remainder(10, 15))
print(remainder(100, 13))
