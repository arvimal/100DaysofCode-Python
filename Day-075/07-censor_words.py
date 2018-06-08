#!/usr/bin/env python3


def censor(text, word):
    """
    Replace word in text with `*`
    """

    word_len = len(word)
    hash_word = "*" * word_len

    if word in text:
        new = text.replace(word, hash_word)
        print(new)
    # print(text)


censor("this hack is wack hack", "hack")
