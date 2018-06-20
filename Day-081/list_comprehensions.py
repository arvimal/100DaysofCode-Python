#!/usr/bin/env python3

my_list = list(range(1, 100))
print(my_list)

clean_list = [i for i in my_list if i % 10 == 0]
print(clean_list)