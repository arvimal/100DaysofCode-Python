#!/usr/bin/env python3

"""
The use-case of this script is to find files with dates in US format
(MM-DD-YYYY) and rename them to EU format (DD-MM-YYYY).

"""
import re
import os
import shutil


def rename_files():
    """
    The steps should ideally be

    1. Create a regex pattern for finding the date format
    2. Get a path as the function argument
    3. Walk the path and search for the pattern
    4. If a pattern match happens, rename the file to the new format

    You will need the `re`, `os`, and `shutil` modules to begin
    """
    date_regex = re.compile(r"""^(.*?)
        ((0|1)?\d)-
        ((0|1|2|3)?\d)-
        ((19|20)?\d\d)
        (.*?)$
        """, re.VERBOSE)
    # print(date_regex)
    os.chdir("/tmp/")
    for file in os.listdir("/tmp/"):
        value = date_regex.search(file)
        if value:
            print(value.groups())
            before = value.group(1)
            month = value.group(2)
            day = value.group(4)
            year = value.group(6)
            after = value.group(8)

            eurofilename = before + day + "-" + month + "-" + year + after

            absPath = os.getcwd()

            amerfilename = os.path.join(absPath, file)
            eurofilename = os.path.join(absPath, eurofilename)
            print("Renaming {} to {}".format(amerfilename, eurofilename))
            shutil.move(amerfilename, eurofilename)
rename_files()
