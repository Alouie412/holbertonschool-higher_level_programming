#!/bin/bash
# This script sends a request to the given URL, feeds the result to wc, and returns the size
# of the body of the response

curl -s "$1" | wc -c
