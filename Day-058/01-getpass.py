#!/usr/bin/env python3

import getpass

try:
    passwd = getpass.getpass()
except Exception as error: 
    print("Hit an exception: {}".format(error))
else:
    print("Password: {}".format(passwd))
