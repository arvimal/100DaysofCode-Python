#!/usr/bin/env python3

# `re.search(pattern, text)` returns an object if the pattern exists
# in the search text.
# But, it is much faster if the search is done on search objects that are
# already compiled.

import re

# Search patterns
pattern_A = "this"
pattern_B = "how"
pattern_C = "that"
pattern_D = "are"

# Text to search the patterns on
text = "Hello, how are you?"

# Create the compiled regex objects
pattern_regex_list = [re.compile(i) for i in [
    pattern_A,
    pattern_B,
    pattern_C,
    pattern_D]
]

for i in pattern_regex_list:
    if i.search(text):
        print("* `{}` found in `{}`".format(i.pattern, text))
    else:
        print("* `{}` not found in `{}`".format(i.pattern, text))
