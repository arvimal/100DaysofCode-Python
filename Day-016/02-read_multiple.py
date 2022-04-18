#!/usr/bin/env python3
# Reading multiple files

import configparser

conf_parser = configparser.ConfigParser()
# The `read()` method takes a list of all files to be read
conf_parser.read(["example_config_1.conf", "example_config_2.conf"])

# In case of reading multiple files, the section being read
# can be present in any of the files.
# This does not ensure the configuration present in a specific file.

# Expecting an output from any of the config files
print(conf_parser.get("main", "cachedir"))
print(conf_parser.get("main", "logfile"))

# Expecting an output from any of the config files
print(conf_parser.get("statd", "debug"))
print(conf_parser.get("statd", "state-directory-path"))
