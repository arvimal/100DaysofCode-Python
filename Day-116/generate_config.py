#!/usr/bin/env python3

import json
import string


with open("data.json", "r") as config:
    data = json.loads(config.read())

print(data)

with open("config.template") as template:
    template = string.Template(template.read())


    