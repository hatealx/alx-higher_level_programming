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
            nl.append(0)
        except ZeroDivisionError:
            print("wrong type")
            nl.append(0)
        except IndexError:
            print("out of range")
            nl.append(0)
        finally:
            nl.append(0)
    return (nl)

