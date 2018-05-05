#!/usr/bin/env python3

# Search for a pattern in a string

import re

# Text to search
text = "Hello, how are you, Are you fine?"

# Patterns to match
pattern_A = "this"
pattern_B = "how"
pattern_C = "that"
pattern_D = "are"

# Create a pattern match object

for i in [pattern_A, pattern_B, pattern_C, pattern_D]:
    match = re.search(i, text)
    if match is not None:
        start = match.start()
        end = match.end()
        print("\nThe search pattern `{}` found in `{}`".format(i, text))
        print(" - Starting position: {}".format(match.start()))
        print(" - Ending position:   {}\n".format(match.end()))
    else:
        print("The search pattern `{}` not found in `{}`".format(i, text))
