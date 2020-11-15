#!/usr/bin/env python3

import re
from re import match
import sys

os_name = ["RHEL"]
major_release = ["8"]
minor_release = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
internal_release = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"]

def release_check(release=None):
    try:
        with open(release) as rel_file:
            rel_val = rel_file.read()
            #print(rel_val)
    except:
        sys.exit(-1)

    release_regex = re.compile(r'(\w{4})(\d).(\d)_v(\d.\d)')
    match_object = release_regex.search(rel_val)
    #print("match_object: {}".format(match_object))

    if match_object == None:
        sys.exit(-2)
    else:
        if all([
            match_object.group(1) == os_name[0],
            match_object.group(2) in major_release,
            match_object.group(3) in minor_release,
            match_object.group(4) in internal_release]
        ):
            print("Valid string: {}".format(match_object.string))
            return True
        else:
            print("Invalid string: {}".format(match_object.string))
            return False

release_check("/tmp/test-release")
