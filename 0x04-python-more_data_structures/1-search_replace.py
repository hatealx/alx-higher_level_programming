#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []

    for num in my_list:
        if num == search:
            newlist.append(replace)
        else:
            newlist.append(num)
    return newlist
