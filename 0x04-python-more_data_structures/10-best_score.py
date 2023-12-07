#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        maxim = -1
        for key, item in a_dictionary.items():
            if item > maxim:
                maxim = item
                keys = key
        return keys
