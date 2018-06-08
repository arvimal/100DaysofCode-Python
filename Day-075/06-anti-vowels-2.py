#!/usr/bin/env python3

def anti_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    text_new = ""

    for i in vowels:
        text_new = text.replace(vowels, "")
    print(text_new)
    # return text_new


# anti_vowels("Hey how are you tuodayu")
anti_vowels("Hey look Words!")
