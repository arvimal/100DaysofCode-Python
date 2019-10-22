#!/usr/bin/env python3

import csv

# Declare the CSV data file
data_file = "examples.csv"

# Open the data file using `with` and `open()`
with open(data_file) as data:

    # Pass the file-descriptor to `csv.reader()`
    # and get the method in return
    data_reader = csv.reader(data)

    # Convert the CSV method `data_reader` as a list
    # for easier parsing.
    # Converting the CSV method to a list gives a list of lists
    # Each list in this list represents a ROW, while each element
    # in each list represent the COLUMN.
    data_lists = list(data_reader)

    # Checking how the list of lists would look like
    print(data_lists)

    # Iterating over the list of lists, and representing
    # the data in a presentable format.

    # This will print the data in the format
    # Plucked <number> <fruit-in-lower-case> on <date time>
    # Plucked 73 apples on 4/5/2015 13:34

    for i in data_lists:
        print("Plucked {1} {2} on {0}".format(i[0], i[2], i[1].lower()))
