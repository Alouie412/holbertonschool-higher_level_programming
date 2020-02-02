#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) is int or type(a) is float or a is NaN:
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if type(b) is int or type(b) is float or b is Nan:
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
