#!/usr/bin/env python3

bday_dict = {}

while True:
    name = input("\nEnter name: ")
    if len(name) != 0 and type(name) == str:
        # Check the existence of the name in bday_dict
        if bday_dict.get(name):
            print("\n{} found in db".format(name))
            print("Name: {}".format(name))
            print("Date  : {}\n".format(bday_dict[name]))
        else:
            print("* {} not found in db, Adding.".format(name))
            new_date = input("* Enter bday date of {}: ".format(name))
            bday_dict[name] = new_date
        print("\nExisting names and b'day dates")
        for _ in bday_dict:
            print("{} : {}".format(_, bday_dict[_]))
    else:
        print("A proper name is required")
