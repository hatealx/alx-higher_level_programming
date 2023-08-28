#!/usr/bin/python3*
def list_division(my_list_1, my_list_2, list_length):
    nl = []
    
    for i in range (0, list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            c = a / b
        except TypeError:
            print("wrong type")
            c = 0
            continue
        except ZeroDivisionError:
            print("division by 0")
            c = 0
            continue
        except IndexError:
            print("out of range")
            c = 0
            break
        finally:
            nl.append(c)
            continue
    return (nl)

