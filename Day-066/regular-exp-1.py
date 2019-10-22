#!/usr/bin/env python3

import re

# 1. Text pattern
ingredient = "Kumquat: 2 cups"
# 2. Generalized pattern
# ingredient = "(ingredient words): (amount digits) (unit words)""

# 3. Create the RE pattern
# a. Replace words with `\w+`
# b. Replace digits with `\d+`
# c. Replace spaces with `\s+`
# d. The colon is left alone since in regular expressions, a colon is
# represented with a colon itself.
# For each field of data, we have used `?P<name>` to identify the data we
# want to extract.

# NOTE: Since regular expressions use `\` frequently, we use raw strings in
# Python to handle this properly. The `r''` prefix tells Python to use the
# string as raw.

# pattern_text = r'(?P<ingredient>\w+):\s+(?P<amount>\d+)\s+(?P<unit>\w+)'

# 4. Compile the Regular expression pattern
# pattern = re.compile(pattern_text)

pattern = re.compile(r"(?P<ingredient>\w+):\s+" r"(?P<amount>\d+)\s+" r"(?P<unit>\w+)")
# 5. Match the pattern against the input text, `ingredient` in this case.
match = pattern.match(ingredient)
print(match.groups())
