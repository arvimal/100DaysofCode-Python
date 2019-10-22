#!/usr/bin/env python3

import csv

data = [
    "first_name, last_name, city".split(","),
    "Harold",
    "Hailey",
    "Peurto Rico".split(","),
    "Blizzy",
    "Blakey",
    "Madagascar".split(","),
]

with open("/tmp/data.csv", "w") as csv_data_file:
    writer = csv.writer(csv_data_file, delimiter=",")
    # print(help(writer))
    for line in data:
        writer.writerow(line)

with open("/tmp/data.csv") as content_file:
    print(content_file.readlines())
