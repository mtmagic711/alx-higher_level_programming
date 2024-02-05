#!/usr/bin/python3
"""Define a function that determine  if the object is exactly
an instance of the specified class"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False
