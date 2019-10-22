#!/usr/bin/env python3

# Writing csv files

import csv

# Write a csv file with three rows and four columns

with open("output.csv", "w") as data_file:
    output_writer = csv.writer(data_file)

    output_writer.writerow(["Hello, World!", "How", "are", "you?"])
    output_writer.writerow(["This", "is", "Sparta", "bitch!"])
    output_writer.writerow(["1", "2", "3", "4"])
