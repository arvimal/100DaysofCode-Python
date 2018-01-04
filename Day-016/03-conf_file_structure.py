#!/usr/bin/env python3

# Use configparser to understand the config file structure

import configparser

conf_parser = configparser.ConfigParser()
conf_parser.read(["example_config_1.conf", "example_config_2.conf"])

for section in conf_parser.sections():
    print("Section: {}".format(section))
    print("\tOptions: {}".format(conf_parser.options(section)))


# This prints
# Section: main
#    Options: ['cachedir', 'keepcache', 'debuglevel', 'logfile', 'exactarch', 'obsoletes', 'gpgcheck', 'plugins', 'installonly_limit']
# Section: statd
#    Options: ['debug', 'port', 'outgoing-port', 'state-directory-path']
