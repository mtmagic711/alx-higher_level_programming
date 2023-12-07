#!/usr/bin/python3
def verify(string):
    if string == 'I':
        return 1
    elif string == 'V':
        return 5
    elif string == 'X':
        return 10
    elif string == 'L':
        return 50
    elif string == 'C':
        return 100
    elif string == 'D':
        return 500
    elif string == 'M':
        return 1000
        
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    num = 0
    i = 0
    while i < len(roman_string) - 1:
        if roman_string[i] == 'I' and roman_string[i + 1] == 'V':
            num += 4
            i += 2
        elif roman_string[i] == 'I' and roman_string[i + 1] == 'X':
            num += 9
            i += 2
        else:
            num += verify(roman_string[i])
            i += 1
    if len(roman_string) != 2:
        num += verify(roman_string[-1])
    return num
