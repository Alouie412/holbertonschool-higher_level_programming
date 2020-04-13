#!/usr/bin/python3
"""
Send a POST request using passed in email and display the
body of the response
"""
import urllib.request
import urllib.parse
import sys


def post_email():
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as msg:
        print(msg.read().decode('utf-8'))

if __name__ == '__main__':
    post_email()
