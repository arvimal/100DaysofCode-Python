#!/usr/bin/env python3

# Count the occurrences of `item` in the sequence.

def count(sequence, item):
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == item:
            count += 1
    print(count)


count([7, 7, 3, 7, 0, 7], 1)
count([4, 'foo', 5, 'foo'],5)