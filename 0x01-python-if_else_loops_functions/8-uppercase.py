#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            print("{}".format(ord(char) - 32), end='')
        else:
            print("{}".format(ord(char)), end='')
        print()
