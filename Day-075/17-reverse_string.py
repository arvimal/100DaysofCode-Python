#!/usr/bin/env python3


def reverse(text):
    """Reverse a give text"""

    reverse_list = []
    for i in text:
        reverse_list.insert(0, i)

    reverse_text = ""
    for i in reverse_list:
        reverse_text += i

    print("{} : {}".format(text, reverse_text))

reverse("ABCD")
reverse("Texting fuckable")
