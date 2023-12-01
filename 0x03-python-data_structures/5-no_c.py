#!/usr/bin/python3

def no_c(my_string):
    string = [ch for ch in my_string if ch not in 'Cc']
    new_string = ''.join(string)
    return new_string
