#!/usr/bin/python3
def print_square(size):
    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    size = int(size)

    for i in range(0, size):
        print('#' * size)
