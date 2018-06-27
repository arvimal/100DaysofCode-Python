#!/usr/bin/env python3

import keyword

print("Keywords in Python programming language.\n")
for i in range(len(keyword.kwlist)):
    print("{}. {}".format(i + 1, keyword.kwlist[i]))
