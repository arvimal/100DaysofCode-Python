#!/usr/bin/env python3

allguests = {
    "Alice": {"apples": 5, "pretzels": 12},
    "Bob": {"ham sandwiches": 3, "apples": 2},
    "Carol": {"cups": 3, "apple pies": 1},
}


def totalBrought(guests, item):
    """
    Calculate the total number of `item`
    brought in by all the guests
    """
    item_count = 0
    for guest, items in allguests.items():
        item_count = item_count + items.get(item, 0)
    print("{:<10}: {}".format(item, item_count))


totalBrought(allguests, "cups")
