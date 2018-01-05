#!/usr/bin/env python3

# The `has_section()` method in the `configparser.ConfigParser()`
# object, helps to check if a particular string exists as a
# section.

# This helps to verify that a section exists, before calling
# the read() method on conf_parser, and can avoid exceptions.

import configparser

conf_parser = configparser.ConfigParser()
conf_parser.read("example_config_1.conf")

# print(conf_parser.has_section("main"))

for i in ["main", "test1", "test", "section", "section1"]:
    print("{0} exists: {1}".format(i, conf_parser.has_section(i)))
