#!/usr/bin/env python3

import getpass
import sys

passwd = getpass.getpass(stream=sys.stderr)
print("You entered: {}".format(passwd))
