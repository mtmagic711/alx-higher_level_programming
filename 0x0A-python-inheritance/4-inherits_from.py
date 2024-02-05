#!/usr/bin/python3
"""A function that determine the subclass"""


def inherits_from(obj, a_class):
    """A function to determine if the object is an instance
    of a class that inherited from the specified class

    Args:
        arg1: the object.
        arg2: the class.

    Returns:
        True or False.
    """

    if issubclass(obj, a_class) and type(obj) != a_class:
        return True
    return False
