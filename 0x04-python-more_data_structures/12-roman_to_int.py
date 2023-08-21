#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {"I": 1, "V": 5, "L": 50, "X": 10, "C": 100, "D": 500, "M": 1000}
    value = 0
    roman_list = list(roman_string)
    for i in range(0, len(roman_list):

                   roman=roman_list[i]
                   equivalent=romans[roman]
                   leng=len(roman_list) - 1))
        if (equivalent > romans[roman + 1]):
            if  ((i <= leng)):
                value += equivalent
        else:
            value -= equivalent
