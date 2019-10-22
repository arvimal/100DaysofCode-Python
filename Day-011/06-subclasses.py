#!/usr/bin/env python3


class Vehicle:
    """Vehicle class"""

    def __init__(self, color, doors, tires, vtype):
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        return "{} braking".format(self.vtype)

    def drive(self):
        print("I am driving a {0} {1}".format(self.color, self.vtype))


"""
if __name__ == "__main__":
    car = Vehicle("Blue", 5, 4, "car")
    print(car.brake())
    print(car.drive())

    truck = Vehicle("Red", 3, 6, "truck")
    print(truck.drive())
    print(truck.brake())
"""


class Car(Vehicle):
    """
    The Car class
    Subclassing from the Vehicle class
    """

    def brake(self):
        """
        We can override the `brake()` method
        inherited from the Vehicle class here.
        """
        print("The brake is dead!")


if __name__ == "__main__":
    car = Car("yellow", 2, 10, "car")
    car.brake()
    car.drive()
