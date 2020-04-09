#!/usr/bin/bash
# This script takes the given URL and sends a GET request, while also feeding it the header
# variable to a specific port

curl -s -H "X-HolbertonSchool-User-Id:98" "$1"
