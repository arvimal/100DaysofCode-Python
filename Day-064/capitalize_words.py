#!/usr/bin/env python3

# Capitalize each word of the sentence, and return it back.
# Do not use the module method `string.capwords()` for this.

sentence = "the big brown fox jumped over the fence"

# Start here
# 1. Create a list of the words, to work on
word_list = sentence.split()

# 2. Work on the word positions, and replace them back
# with the capitalized ones.
for i in range(0, len(word_list)):
    word_list[i] = word_list[i].capitalize()

# 3. Create updated sentence from the capitalized word list
cap_sentence = " ".join(word_list)

# 4. Verify the results
print("Initial state: {}".format(sentence))
print("Final state:   {}".format(cap_sentence))
print()

# Using the `string.capwords()` method
import string

print("- Using the `string.capwords()` method.")
print("Initial state: {}".format(sentence))
print("Final state:   {}".format(string.capwords(sentence)))
