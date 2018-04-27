#!/usr/bin/env python3

import textwrap

# 1. Our text to work on.

dummy_text = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen
ok. It has survived not only five centuries, but also the leap into electronic
typesetting, remaining essentially unchanged. It was popularised in the 1960s with
the release of Letraset sheets containing Lorem Ipsum passages, and more recently
with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

# 2. Using the `textwrap` module to parse the text
dedented_text = textwrap.dedent(dummy_text)
print("1. The text after removing the indentation:")
print(dedented_text)
print("\n2. The text after setting a line width of 70 chars:")
print(textwrap.fill(dedented_text, width=70))

