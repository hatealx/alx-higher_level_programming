#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    unique = []
    for num in my_list:
        if num not in unique:
            add += num
            unique.append(num)
    return add
