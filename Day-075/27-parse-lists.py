#!/usr/bin/env python3

"""
1) Write a function to take out duplicates and title case them.
2) Sort the list in alphabetical descending order by surname.
3) Determine what the shortest first name is.

For this exercise you can assume there is always one name and one surname.
"""

NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    NAMES_NEW = []
    for name in NAMES:
        if name.title() not in NAMES_NEW:
            NAMES_NEW.append(name.title())
        else:
            pass
    return NAMES_NEW


def shortest_first_name(names):
    names = dedup_and_title_case_names(names)
    name_by_len = sorted(names, key=len)
    first_name = []
    for i in name_by_len:
        first, last = i.split(" ")
        first_name.append(first)
        sorted_first = sorted(first_name, key=len)
    # print(sorted_first)
    return sorted_first[0]
    # ...


print(dedup_and_title_case_names(NAMES))
print(shortest_first_name(NAMES))
