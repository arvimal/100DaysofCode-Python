def quick_sort(num_list):
    """
    Quick sort in Python
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


num_list = [9, 1, 2, 3, 8, 5, 4]
print(quick_sort(num_list))
