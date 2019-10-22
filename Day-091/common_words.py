#!/usr/bin/env python3

"""Find the common words in both the strings"""


def contains(big_string, little_string):
    if little_string in big_string:
        return True
    else:
        return False


def common_letters(string_one, string_two):
    common_words = []
    for i in string_one:
        if i in string_two:
            if i in common_words:
                pass
            else:
                common_words.append(i)
    print(common_words)
    return common_words


common_letters("manhattan", "san francisco")
