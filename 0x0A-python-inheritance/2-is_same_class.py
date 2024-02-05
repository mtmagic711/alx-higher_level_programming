#!/usr/bin/python3
"""define a  function that returns True if the object
is exactly an instance of the specified class"""

def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    return False
