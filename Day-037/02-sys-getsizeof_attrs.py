#!/usr/bin/env python3

import sys


class MyClass:
    pass


class MyNewClass:
    def __init__(self):
        self.name = "name"
        self.age = "age"
        self.num = "num"

    def test(self):
        list_1 = [1, 2, 3, 4, 5]
        tup_1 = (1, 2, 3, 4, 5)
        list_2 = list_1
        tup_2 = tup_1


my_class = MyClass()
my_new_class = MyNewClass()

print(f"Size of class object w/o atts: {sys.getsizeof(my_class)}")
print(f"Size of class object with attrs: {sys.getsizeof(my_new_class)}")
