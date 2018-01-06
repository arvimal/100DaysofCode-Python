#!/usr/bin/env python3

import configparser

conf_parser = configparser.ConfigParser()
conf_parser.read("example_config_1.conf")

# The `get()` method gets every values as strings.
# This is convenient, and the values can be converted
# after retrieving the value.

# `getfloat()` checks for floats
# `getint()` checks for ints,
# `getboolean()` checks for boolean conditions

print(conf_parser.getfloat("main", "exactarch"))

# Using a get method on a different return type
# will print an error.

print(conf_parser.getfloat("main", "logfile"))
