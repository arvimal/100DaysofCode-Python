#!/usr/bin/env python3

# Use configparser to understand the config file structure

import configparser

conf_parser = configparser.ConfigParser()
conf_parser.read(["example_config_1.conf", "example_config_2.conf"])

for section in conf_parser.sections():
    print("Section: {}".format(section))

# The `options()` method returns a list of options under each section.
# This prints
# Section: main
#    Options: ['cachedir', 'keepcache', 'debuglevel', 'logfile', 'exactarch', 'obsoletes', 'gpgcheck', 'plugins', 'installonly_limit']
# Section: statd
#    Options: ['debug', 'port', 'outgoing-port', 'state-directory-path']
    print("\tOptions: {}".format(conf_parser.options(section)))

# The `items()` method for conf_parser returns a dictionary,
# with the items under each section and its values.
    print("Options and corresponding Values in the configuration file")
    for option, values in conf_parser.items(section):
        print(" {}: {}".format(option, values))
