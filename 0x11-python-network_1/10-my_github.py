#!/usr/bin/python3
""" Display the id of a Github user using Github's API """
import requests
import sys


def get_hub():
    """ Get the id of the user using their personal access token password """
    req = requests.get("https://api.github.com/user", auth=(sys.argv[1], sys.argv[2]))
    print(req.json().get('id'))


if __name__ == '__main__':
    get_hub()
