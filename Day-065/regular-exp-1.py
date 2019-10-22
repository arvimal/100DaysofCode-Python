#!/usr/bin/env python3

import re

# 1. The pattern and the text to search for the pattern
pattern = "this"
text = "Does this text match the pattern?"

# 2. Create the search object, and pass the pattern/text
match = re.search(pattern, text)

# 3. The `match` object has several methods which can
# show information on the searched string.
start = match.start()
end = match.end()

print(
    "Found: `{}`\nIn: `{}`\nAt position: {} to {}".format(
        match.re.pattern, match.string, start, end
    )
)
