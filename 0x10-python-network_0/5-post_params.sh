#!/usr/bin/bash
# This script sends a POST request to the given URL and returns the result

curl -S "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
