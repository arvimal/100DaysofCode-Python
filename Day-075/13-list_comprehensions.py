#!/usr/bin/env python3

# 1. Print all numbers from 1 to 10
print([i for i in range(1, 11)])

# 2. Print all odd numbers from 1 to 10
print([i for i in range(1, 11) if i % 2 != 0])

# 3. Create a list of squared values, for the numbers from 1 to 10
print([i ** 2 for i in range(1, 11)])

# 4. Create a list of squared values, for the odd numbers from 1 to 10.
print([i ** 2 for i in range(1, 11) if i % 2 != 0])

# 5. Create a list for the numbers fully divisible by 3, between 1 and 10.
print([i for i in range(1, 11) if i % 3 == 0])

# 6. Print the cubes of the numbers 1 through 10 only if the cube is evenly divisible by four.
print([i ** 3 for i in range(1, 11) if (i ** 3) % 4 == 0])

# 7. List the methods in the namespace of an object, omitting special/magic methods
def dir_listing(obj):
    return [i for i in dir(obj) if not i.startswith("__")]


# 8. Convert a list of strings to integers
x = ["1", "2", "3", "4", "5"]
y = [int(k) for k in x]
print(y)
print(type(y[1]))

# 9. Strip a list of strings from leading/ending whitespace
myStringList = [" Hello", "World  "]
print(myStringList)
myStrings = [s.strip() for s in myStringList]
print(myStrings)
