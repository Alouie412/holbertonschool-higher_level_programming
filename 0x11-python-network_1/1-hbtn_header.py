#!/usr/bin/python3
""" Get the X-Request-ID of the passed in website argument """
import urllib.request
import sys


def response_header():
    with urllib.request.urlopen(sys.argv[1]) as req:
        print(req.getheader('X-Request-ID'))

if __name__ == '__main__':
    response_header()
