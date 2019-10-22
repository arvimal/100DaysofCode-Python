#!/usr/bin/env python3

birthdays = {"Alice": "April 1", "Bob": "December 12", "Carol": "March 4"}

while True:
    name = input("\nEnter a name [blank to quit]: ")
    if name == "":
        break

    if name in birthdays.keys():
        # birthdays or birthdays.keys() iterate through keys
        print("{}'s birthday is on {}\n".format(name, birthdays[name]))
    else:
        print("Name does not exist in database!")
        birth_date = input("When is your friend's birthday? ")
        birthdays[name] = birth_date
        print("Birthday date for {} updated!".format(name))
