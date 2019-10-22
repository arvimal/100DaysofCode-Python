#!/usr/bin/env python3

# My cats

my_cats = []
number = 0

number = int(input("\nHow many cats do you have?: "))
print("\nPlease name the {} cats -\n".format(number))
for i in range(number):
    name = input("Cat {0} : ".format(i))
    my_cats.append(name)

print("\nYour cats are: ")
for cat in my_cats:
    print(cat)
