#!/usr/bin/python3
"""
Send a request to the passed in url and display the body of the response
If it fails for whatever reason, display the status code. Requests version
"""
import requests
import sys


def error():
    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)


if __name__ == '__main__':
    error()
