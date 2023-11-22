#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        f = i % 3
        b = i % 5

        if ((f == 0) and (b == 0)):
            print("FizzBuzz", end=" ")
        elif (f == 0):
            print("Fizz", end=" ")
        elif (b == 0):
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
