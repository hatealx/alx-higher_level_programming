#!/usr/bin/python3
from calculator_1 import add, mul, sub, div
from sys import argv
import sys


def main():
    operators = "+/*-"
    if (len(argv) < 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if (operator not in operators):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    res = 0
    if (operator == "+"):
        res = add(a, b)
        print(f"{a} + {b} = {res}")
        sys.exit(0)
    elif (operator == "*"):
        res = mul(a, b)
        print(f"{a} * {b} = {res}")
        sys.exit(0)
    elif (operator == "-"):
        res = sub(a, b)
        print(f"{a} - {b} = {res}")
        sys.exit(0)
    else:
        res = div(a, b)
        print(f"{a} / {b} = {res}")
        sys.exit(0)


if __name__ == "__main__":
    main()
