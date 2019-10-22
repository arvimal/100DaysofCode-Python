#!/usr/bin/env python3

# Question:
# Given a paragraph, clean it from any new line characters, tabs etc, and print
# each line in the paragraph in a single line.

import textwrap

dummy_text = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen
ok. It has survived not only five centuries, but also the leap into electronic
typesetting, remaining essentially unchanged. It was popularised in the 1960s with
the release of Letraset sheets containing Lorem Ipsum passages, and more recently
with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

# Remove newline characters from dummy_text
# strip() (or strip("\n")) only replaces text/characters at
# the start and end of the string.
# In order to remove all the occurrences, use `string.replace()`
cleaned_text = dummy_text.replace("\n", " ")
# Strip of any unwanted whitepsaces, especially the one at the start.
print(cleaned_text.strip())

# To print each sentence in the paragraph in its own line, we can
# split them to a list with `.` as the delimiter, and print from the list.
print("\nPoints:")
sentence_list = cleaned_text.split(".")
print(sentence_list)
for i in range(0, len(sentence_list) - 1):
    print("{}. {}.".format(i + 1, sentence_list[i]))
