#!/usr/bin/env python3.6

from collections import ChainMap

dict_1 = {"One": 1, "Two": 2, "Three": 3}
dict_2 = {"Four": 4, "Five": 5, "Six": 6}
dict_3 = {"Seven": 7, "Eight": 8, "Nine": 9}

all_dicts = ChainMap(dict_1, dict_2, dict_3)

print(all_dicts["Five"])
print(all_dicts["Seven"])
