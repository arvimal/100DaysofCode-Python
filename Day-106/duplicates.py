#!/usr/bin/env python3

def find_dupes(num=[]):
    num_dict = {}
    if len(num) in [0, 1]:
        print("We need a list with more than one number.")
        exit()
    else:
        for i in range(len(num) + 1):
            if num[i] in num_dict.keys():
                pass
            else:
                num_dict.item()

    print(num_dict)

find_dupes([1,2,2,2,3,4,5])