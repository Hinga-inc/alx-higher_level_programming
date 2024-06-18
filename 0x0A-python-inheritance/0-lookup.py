#!/usr/bin/python3
def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj (any): object of any type

    Returns:
        list of available attributes and methods

    """
    return [i for i in dir(obj)]
