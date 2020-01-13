#!/usr/bin/env python3

# Algorithm: Quick sort
# Referrence: https://github.com/TheAlgorithms/Python/blob/master/sorts/quick_sort.py



def quick_sort(num_list):
    """
    Quick sort in Python

    If length of the list is 1 or less, there is no point in sorting it.
    Hence, the code works on lists with sizes greater than 1
    """
    
    if len(num_list) <= 1:
        return(num_list)
    else:
        pivot = num_list.pop()
        less_than = []
        greater_than = []
        for num in num_list:
            if num < pivot:
                less_than.append(num)
            elif num > pivot:
                greater_than.append(num)
    #print(less_than)
    #print(pivot)
    #print(greater_than)
    return quick_sort(less_than) + [pivot] + quick_sort(greater_than)


num_list = [10, -1, 100, 23, 5, 98, 45, 76, -545, -300, 9999]
print(quick_sort(num_list))
