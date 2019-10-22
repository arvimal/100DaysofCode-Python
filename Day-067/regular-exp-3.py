#!/usr/bin/env python3

# The `re.search(pattern, text)` can only search for single instances of text.
# REFER `Day-067/regular-exp-1.py`

# To find multiple occurrences, use `re.findall()`

import re

# Text to search
text = "Hello, how are you, Are you fine?"

# Patterns to match
pattern_A = "this"
pattern_B = "how"
pattern_C = "that"
pattern_D = "are"
