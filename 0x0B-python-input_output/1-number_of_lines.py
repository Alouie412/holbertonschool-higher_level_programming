#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, 'r') as f:
        return sum(1 for i in f)
