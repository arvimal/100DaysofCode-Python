#!/usr/bin/env python3

# Everything in Python are objects.
# This means that everything that's created is an
# instance on a pre-defined class, or a self-defined class.
# These instances are in memory (hence named objects), and
# has access to the functions defined in the original classes
# and is called methods.

# 1. Creating a name in the namespace
# This example shows creating a variable.
# Know that this variable `name` is created as an instance
# of the str() class.
name = "Rob"
print(type(name))
print(dir(name))

# 2. Creating a custom class


class Animal:
    """Animal Class"""

    def __init__(self):
        """Constructor for Animal Class"""
        pass

    def print_name(self, name):
        print("{} is an Animal".format(name))


# Creating an instance out of Animal class
my_animal = Animal()
my_animal.print_name("Deer")

# 3. self
# `self` is a contruct which refers to the instance
# of the class itself.


class Vehicle:
    """Vehicle class"""

    def __init__(self, color, doors, tires, vtype):
        self.color=color
        self.doors=doors
        self.tires=tires
        self.vtype = vtype

    def brake(self):
        return "{} braking".format(self.vtype)

    def drive(self):
        return "I am driving a {0} {1}".format(self.color, self.vtype)

if __name__ == "__main__":
    car = Vehicle("Blue", 5, 4, "car")
    print(car.brake())
    print(car.drive())

    truck = Vehicle("Red", 3, 6, "truck")
    print(truck.drive())
    print(truck.brake())