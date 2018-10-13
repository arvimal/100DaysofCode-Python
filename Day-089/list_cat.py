#!/usr/bin/env python3


def concat(my_list):
    """
    Concatenate the items in the list
    into a sentence, separated by comma.
    """
    my_output = ""

    for elem in my_list:
        # O(n)
        if elem == my_list[-2]:
            my_output += str(elem)
            my_output += ", and "
        elif elem == my_list[-1]:
            my_output += str(elem)
        else:
            my_output += str(elem)
            my_output += str(", ")
    print(my_output)


concat(["one", "two", "three"])
concat(["one", "two", "three", "four"])
concat(["you", "me", "him", "they", "them"])
concat(["a", "e", "i", "o", "u"])