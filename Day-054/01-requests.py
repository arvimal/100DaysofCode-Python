# /usr/bin/env python3

import requests
import pprint

conn = requests.get("https://wwww.google.com")
pprint.pprint(dir(conn))
