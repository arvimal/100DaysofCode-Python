#!/usr/bin/env python3

# The `has_option()` helps to check for options
# within sections.

import configparser

conf_parser = configparser.ConfigParser()
conf_parser.read("example_config_1.conf")

for i in ["main", "test1", "test", "section", "section1"]:
    has_section = conf_parser.has_section(i)
    for j in ["keepcache", "gpgcheck"]:
        has_option = conf_parser.has_option(i, j)
        print('{}.{:<12}  : {}'.format(i, j, has_option))