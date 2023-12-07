#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dic = {key: item*2 for key, item in a_dictionary.items()}
    return new_dic
