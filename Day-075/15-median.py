#!/usr/bin/env python3


def median(data):
    """Finding the median from a list"""
    # 1. Sort the list
    new_data = sorted(data)

    if len(new_data) == 1:
        print(new_data[0])
        return new_data[0]
    else:
        # Odd
        if len(new_data) % 2 == 1:
            mid_value = len(new_data) // 2
            print(new_data[mid_value])
            return new_data[mid_value]
        # Even
        elif len(new_data) % 2 == 0:
            mid_value = len(data) // 2
            median_val = (new_data[mid_value] + new_data[mid_value - 1]) / 2.0
            print(median_val)
            return median_val


median([10, 5, 3, 7, 8, 23])
