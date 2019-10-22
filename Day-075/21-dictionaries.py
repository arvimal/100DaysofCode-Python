#!/usr/bin/env python3

# Dictionaries map a value to a key, hence a value can be
# called using the key.

# 1. They ar3333i3ie mutable, ie. they can be changed.
# 3. They are surrounded by curly {} brackets.
# 3. They are indexed using square [] brackets.
# 4. Key and Value pairs are separated by columns ":"
# 5. Each pair of key/value pairs are separated by commas ",".
# 6. Dicts return values not in any order.
# 7. collections.OrderedDict() gives an ordered dictionary.

# Create a dict
mydict1 = {}

# Add values to the dict.
mydict1["host1"] = "A.B.C.D"
mydict1["host2"] = "E.F.G.H"
print(mydict1)

# Remove values
del mydict1["host2"]
print(mydict1)

# Check if a key exists in a dict.
"host2" in mydict1
"host1" in mydict1

# Add elements to the dictionary
mydict1["host3"] = "I.J.K.L"
mydict1["host4"] = "M.N.O.P"
print(mydict1)

# Check the length of the dictionary
print(len(mydict1))
print(mydict1.keys())

released = {
    "IPhone": 2007,
    "IPhone 3G": 2008,
    "IPhone 3GS": 2009,
    "IPhone 4": 2010,
    "IPhone 4S": 2011,
    "IPhone 5": 2012,
    "IPhone 5s": 2013,
    "IPhone SE": 2016,
}

for i, j in released.items():
    print("{0} was released in {1}".format(i, j))

# Change a value for a specific key
print("Changing the value for a key")
released["IPhone"] = 2006
released["IPhone"] += 1
print(released["IPhone"])
released["IPhone"] -= 1
print(released["IPhone"])
