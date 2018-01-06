#!/usr/bin/env python3

# Print all Sections and Options in a pretty format.

import configparser

conf_parser = configparser.ConfigParser()
conf_parser.read("example_config_2.conf")

print("Printing Sections and corresponding Options:")
for section in conf_parser.sections():
    print("\t[{}]".format(section))
    print("\t\t{}".format(conf_parser.options(section)))

