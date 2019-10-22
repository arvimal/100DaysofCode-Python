#!/usr/bin/env python3

import sys


class MyClass:
    def __init__(self):
        self.name = "name"
        self.num = "num"

    def __sizeof__(self):
        print(self.__dict__.values())
        # return object.__sizeof__(self) + sum(sys.getsizeof(v) for v in self.__dict__.values())


my_class = MyClass()
print(sys.getsizeof(my_class))
