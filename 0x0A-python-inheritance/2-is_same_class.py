#!/usr/bin/python3
"""
This technically works too, but would also return True for
checking if a_class is object. Not wrong, but not the desired
output

def is_same_class(obj, a_class):
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
"""

def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
        return False
