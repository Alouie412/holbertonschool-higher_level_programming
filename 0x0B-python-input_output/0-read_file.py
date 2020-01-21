#!/usr/bin/python3
def read_file(filename=""):
    """
    This set of code would work for opening and reading a file, but the
    instructions state that the with statement must be used
    f = open('filename', 'r')
    f.read()
    f.close()
    """

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
