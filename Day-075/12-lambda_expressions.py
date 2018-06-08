#!/usr/bin/env python3

# Lambda functions are expressions which return a value, and not statements.
# Hence, it doesn't accept `print`, `return` etc.

# 1. Add two numbers
add = lambda x, y: return x + y
add(4,2)
# 2. Create a list, squares, that consists of the squares of the numbers 1 to 10. A list comprehension could be useful here!
# Use filter() and a lambda expression to print out only the squares that are between 30 and 70 (inclusive).
squares = [i**2 for i in range(1, 11)]
print filter(lambda x: x >= 30 and x <= 70, squares)

# 3. Use a list comprehension to create a list, threes_and_fives, that consists only of the numbers
# between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.
threes_and_fives = [i for i in range(1, 16) if i % 3 == 0 or i % 5 == 0]
print(threes_and_fives)

# 4. Strip the `X` from the string, using a lamda function which gets passed to a filter method.
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x.strip("X"), garbled)
print(message)