def divisible_by_2(my_list=[]):
    li = []

    for num in my_list:
        if num % 2 == 0:
            li.append(True)
        else:
            li.append(False)
    return li
