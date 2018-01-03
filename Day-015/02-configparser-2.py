#!/usr/bin/env python3

import configparser

# Defining the configuration file
path = "config_file_1.conf"

# Creating the `config` object from `configparse`
config = configparser.ConfigParser()
# Reading from the configuration file
config.read(path)

# Read a couple of existing configurations,
# under the `Settings` section.
font = config.get("Settings", "font")
font_size = config.get("Settings", "font_size")

# Change/Set a couple of configurations under the
# `Settings` section. The same syntax is also used
# to create new ones.
config.set("Settings", "font_size", "15")
config.set("Settings", "font", "monaco")

# Remove a configuration under `Settings`
config.remove_option("Settings", "font_style")

# Open the configuration file, and write the
# new changes.
with open(path, "w") as config_file:
    config.write(config_file)
