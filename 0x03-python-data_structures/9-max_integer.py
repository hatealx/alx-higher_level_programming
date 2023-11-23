#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    elif len(my_list) == 1:
        return my_list[0]
    else:
        bigest = my_list[0]
        for i in range(1, len(my_list)):
            if bigest < my_list[i]:
                bigest = my_list[i]
            else:
                continue
        return bigest
