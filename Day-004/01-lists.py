#!/usr/bin/env python3

# Sorting a list.
# Sorting changes the original list
# Remember that lists are mutable, ie. can be changed.
list_1 = [100, 99, 34, 3, 4, 77]
print("list_1 : {0}".format(list_1))
list_1.sort()
print("list_1 sorted : {0}".format(list_1))

# Assigning the sorting of a list to another doesn't work
list_2 = [35, 45, 32, 11, 99]
print("\nlist_2 : {}".format(list_2))
list_3 = list_2.sort()
print("list_2 sorted : {0}".format(list_3))

print("Hello, world!")
list_4 = [i for i in range(10)]
print(list_4)
