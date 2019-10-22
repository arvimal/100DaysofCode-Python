#!/usr/bin/env python3

# This example
# 1. Creates a configuration file
# 2. Reads a config file
# 3. Get the settings
# 4. Update/Set new values
# 5. Delete existing settings

import configparser
import os


def create_config(path):

    config = configparser.ConfigParserconfig.set("GLOBAL", "interface_name", "ensp01")
    config.add_section("GLOBAL")
    config.set("GLOBAL", "interface_name", "ensp01")
    config.set("GLOBAL", "interface_ip", "192.168.10.1")

    with open(path, "w") as config_file:
        config.write(config_file)


def get_config(path):
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_settings(path, section, setting):
    config = get_config(path)
    value = config.get(section, setting)
    print("In Section {0}, {1} is {2}".format(section, setting, value))
    return value


def update_setting(path, section, setting, value):
    config = get_config(path)
    config.set(section, setting, value)
    with open("path", "w") as config_file:
        config.write(config_file)


def delete_setting(path, section, setting):
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config_write(config_file)


if __name__ == "__main__":
    path = "config_file_2.conf"
    font = get_settings(path, "Settings", "font")
    font_size = get_settings(path, "Settings", "font_size")
    update_setting(path, "Settings", "font_size", "12")
    delete_setting(path, "Settings", "font_style")
