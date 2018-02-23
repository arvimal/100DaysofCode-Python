#!/usr/bin/env python3

import getpass

passwd = getpass.getpass(prompt="Enter new password: ")
passwd = passwd.lower()

if passwd == "password":
    print("Password correct.\n")
else:
    print("Try again!")
