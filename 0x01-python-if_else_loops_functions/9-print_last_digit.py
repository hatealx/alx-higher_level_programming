#!/usr/bin/python3
def print_last_digit(number):
    if (number > 0):
        last = number % 10
        print(last, end="")
        return (last)
    elif (number < 0):
        last = (-number) % 10
        print(last, end="")
        return (last)
    else:
        print(0, end="")
        return (0)
