#!/usr/bin/env python3

# Find the occurrences of each word in the following sentence.
# Return the word and the number of occurrences.

sentence = """
Nathan Pinchback Tomer, who adopted the name Jean Tomer early
in his literary career, was born in Washington, D.C. in 1894.
Jean is the son of Nathan Tomer was a mixed-race freedman,
born into slavery in 1839 in Chatham County, North Carolina.
Jean Tomer is most well known for his first book Cane,
which vividly portrays the life of African-Americans in southern
farmlands.
"""

from pprint import pprint
from textwrap import TextWrapper

word_dict = {}

sentence_list = sentence.split()

for word in sentence_list:
    if word in word_dict.keys():
        word_dict[word] += 1
    else:
        word_dict[word] = 1

# pprint(word_dict)

for key in word_dict:
    print("{:<20} : {:<5}".format(key, word_dict[key]))
