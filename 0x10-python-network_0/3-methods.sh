#!/bin/bash
# Queries a URL passed to the script with a OPTIONS request and displays the body of the response
curl -sX OPTIONS "$1"
