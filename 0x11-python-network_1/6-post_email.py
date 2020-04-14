#!/usr/bin/python3
"""
Send a POST request using passed in email and display the
body of the response. Requests version
"""
import requests
import sys


def post_email():
    new_dict = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], new_dict)
    print(req.text)


if __name__ == '__main__':
    post_email()
