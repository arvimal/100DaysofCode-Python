#!/usr/bin/env python3


def anti_vowels(text):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    text_list = list(text)

    # Remove vowels
    # pdb.set_trace()
    for pos in range(len(text_list)):
        for i in text_list:
            # print("Iterating {}".format(i))
            if i in vowels:
                # print("{} is present in {}".format(i, vowels))
                # print("Removing {}".format(i))
                text_list.remove(i)
                # print(text_list)

    # Create the string back from the list
    text_new = ""
    for i in text_list:
        text_new += i
    print(text_new)


# anti_vowels("Hey how are you tuodayu")
anti_vowels("Hey look Words!")
anti_vowels("Hey, how are you today?")
