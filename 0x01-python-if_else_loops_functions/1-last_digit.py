#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    t = -(number)
    r = -(t % 10)
else:
    r = number % 10


if (r > 5):
    print(f"Last digit of {number} is {r} and is greater than 5")
elif ((r < 6) and (r != 0)):
    print(f"Last digit of {number} is {r} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {r} and is 0)
