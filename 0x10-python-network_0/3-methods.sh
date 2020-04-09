#!/usr/bin/bash
# This script takes in the given URL and displays all allowed HTTP methods on the server
# Note that cut uses --complement, to exclude 'Allow', as 'Allow' is not an HTTP method

curl -si -X OPTIONS "$1" | grep 'Allow' | cut -d ' ' --complement -f1
