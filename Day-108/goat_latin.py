#!/usr/bin/env python3

"""
https://leetcode.com/problems/goat-latin/

824. Goat Latin - Easy

A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.

Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"


Notes:

S contains only uppercase, lowercase and spaces. Exactly one space between each word.
1 <= S.length <= 150

"""


class Solution:
    def toGoatLatin(self, S: str) -> str:
        word_list = S.split()
        goat_word = []
        for word in word_list:
            index = word_list.index(word)
            if word[0].lower() in ["a", "e", "i", "o", "u"]:
                j = word + "ma" + str((index + 1) * "a")
                goat_word.append(j)
            else:
                k = word[1:] + word[0] + "ma" + str((index + 1) * "a")
                goat_word.append(k)
            final_line = ""
            for i in goat_word:
                final_line = final_line + i + " "
        print(goat_word)
        return final_line.strip()

Test = Solution()
Test.toGoatLatin("I speak Goat Latin")
Test.toGoatLatin("A x gij T Ka Stsl UTK kqdc A")
