#!/bin/bash
# Queries a URL passed to the script with a DELETE request and displays the body of the response
curl -sX DELETE "$1"
