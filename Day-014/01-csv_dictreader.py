#!/usr/bin/env python3

import csv

with open("examples.csv") as data_file_obj:
    reader = csv.DictReader(data_file_obj, delimiter = ",")
    print("\nNames: ")
    for line in reader:
        print("{0} {1}".format(line["first_name"], line["last_name"]))

