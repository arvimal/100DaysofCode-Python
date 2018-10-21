#!/usr/bin/env python3


toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early
in his literary career, was born in Washington, D.C. in 1894.
Jean is the son of Nathan Tomer was a mixed-race freedman,
born into slavery in 1839 in Chatham County, North Carolina.
Jean Tomer is most well known for his first book Cane,
which vividly portrays the life of African-Americans in southern
farmlands.
"""

toomer_list = toomer_bio.split()
#print(toomer_list)
for word in toomer_list:
    print(word)
    # NOTE:
    # Had to change the first `if` statement since
    # the first occurrence of `Tomer` had a comma in
    # the list element as part of it.
    # This made the first occurrence of `Tomer` stay
    # the same.
    # Hence, we use "Tomer" in word:
    #if word == "Tomer":
    if "Tomer" in word:
        print("\nFound one\n")
        word_index = toomer_list.index(word)
        toomer_list[word_index] = "Toomer"
print(toomer_list)