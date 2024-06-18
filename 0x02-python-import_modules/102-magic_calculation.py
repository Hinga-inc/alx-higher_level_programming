#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        x = add(a, b)
        for i in range(4, 6):
            x = add(x, i)
        return x
    else:
        return sub(a, b)
