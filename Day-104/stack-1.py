#!/usr/bin/env python3

# Stacks in Python using lists
import random

class Stack():
    """
    Stack class
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        self.items.pop(item)

    def get_stack(self):
        return self.items



stack_1 = Stack()
for i in range(1, 25):
    j = random.randint(1, 25)
    stack_1.push(j)

print("Stack 1: {}".format(stack_1.get_stack()))