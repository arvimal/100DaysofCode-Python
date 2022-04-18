#!/usr/bin/env python3

import configparser

# Specify a variable with the configuration file name
conf_file = "example_config_1.conf"

# Create an object of `configparser.ConfigParser()`
# NOTE: Before parsing a file, the `configparser.ConfigParser()` object
# has to execute the read() method on the configuration file.
# Else, it won't be able to parse it.
# The catch here is, there is no object to which the read() method
# is assigned.
conf_parser = configparser.ConfigParser()
conf_parser.read(conf_file)

print(conf_parser.get("main", "debuglevel"))
print(dir(conf_parser))
