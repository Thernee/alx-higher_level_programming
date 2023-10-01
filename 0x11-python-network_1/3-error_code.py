#!/usr/bin/python3

"""Uses urllib to send a request to a url and capture the HTTP error codes"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
