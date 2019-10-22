#!/usr/bin/env python3

"""
1. Create a list of author names from the string.
2. Create a second list with the last names of the authors.
"""

authors = "Audre Lorde, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

# 1. Author names as a list
author_names = authors.split(",")
print(author_names)

# 2. Last names of Authors
author_last_names = []
for name in author_names:
    author_last_names.append(name.split(" ")[-1])
print(author_last_names)
