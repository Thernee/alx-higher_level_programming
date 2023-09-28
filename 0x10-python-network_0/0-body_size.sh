#!/usr/bin/env bash
# Queries a URL passed to the script and displays the size of the body

curl -i "$1" | grep -i "Content-Length" | awk '{print $2}'
