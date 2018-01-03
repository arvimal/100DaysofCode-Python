#!/usr/bin/env python3

# The `configparser` parser helps to parse INI files.
# It can be used to read and write configuration files.

import configparser

# Set the configuration file name to `config_file_1.conf`
config_file = "config_file_1.conf"

# Open the `config` object from configparser.ConfigParser
config = configparser.ConfigParser()

# Add a section, ie. an INI section
config.add_section("Settings")

# Add configurations, under the section defined in
# the first field.
config.set("Settings", "font", "Courier")
config.set("Settings", "font_size", "10")
config.set("Settings", "font_style", "Normal")

# Open the file in `w` mode and write the configurations.
with open(config_file, "w") as config_file:
    config.write(config_file)


