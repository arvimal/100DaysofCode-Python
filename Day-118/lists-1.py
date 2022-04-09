#!/usr/bin/env python3

bicycles = ["trek", "cannondale", "redline", "specialized"]
print("{}\n".format(bicycles))
print("{} Object type: {}".format("bicycles", type(bicycles)))

print(bicycles[0])


for bike in bicycles:
    print(bike.title())
