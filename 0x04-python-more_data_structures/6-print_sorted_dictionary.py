#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    dic = dict(a_dictionary)
    for key, item in sorted(dic.items()):
        print("{}: {}".format(key, item))
