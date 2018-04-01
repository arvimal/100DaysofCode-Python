#!/usr/bin/env python3

import pwd
import sys

username = sys.argv[1]
user_info = pwd.getpwnam(username)

print("Username: {}".format(user_info.pw_name))
