#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    li1 = list(set_1)
    li2 = list(set_2)
    for el in li1:
        if el in li2:
            li1.remove(el)
            li2.remove(el)
    return (set(li1) | set(li2))
