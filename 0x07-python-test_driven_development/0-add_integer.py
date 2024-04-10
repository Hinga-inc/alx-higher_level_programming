def add_integer(a, b=98):
    """Func that adds two ints

    Args:
        a ((int, (float)): first arg to add to sum.
        b ((int, (float)): second arg to add to sum. Defaults to 98.

    Returns: sum of both values.

    """
    if type(a) is float:
        a = int(a)
    elif type(a) is not int:
        raise TypeError('a must be an integer')

    if type(b) is float:
        b = int(b)
    elif type(b) is not int:
        raise TypeError('b must be an integer')

    return a + b
