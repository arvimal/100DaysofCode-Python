#!/usr/bin/env python3

import logging

def add(x, y):
    logging.info("{} + {} = {}".format(x, y, x + y))
    return  x + y
