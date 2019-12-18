#!/usr/bin/python3
def no_c(my_string):f
    my_string = ''.join(i for i in my_string if i != 'c' and i != 'C')
    return my_string
