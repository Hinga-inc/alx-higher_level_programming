#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """Function that prints "My name is ", followed by the one or two string \
arguments given.

    Args:
        first_name (str): string representing first name
        last_name (str): string representing last name

    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is " + first_name, end="")
    if first_name is not "":
        print(" ", end="")
    print(last_name)

