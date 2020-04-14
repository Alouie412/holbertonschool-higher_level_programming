#!/usr/bin/python3
"""
Send a request to the passed in url and display the body of the response
If it fails for whatever reason, display the status code
"""
import urllib.request
import sys


def error():
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as msg:
            print(msg.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        #print("Error code: {}".format(err.read().decode('utf-8')))
        print("Error code: {}".format(err.code))

if __name__ == '__main__':
    error()
