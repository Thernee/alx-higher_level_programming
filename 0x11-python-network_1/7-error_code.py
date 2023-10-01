#!/usr/bin/python3

"""sends request to a URL and displays body of the response, or error"""
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code < 400:
        print(req.text)
    else:
        print(f"Error code: {req.status_code}")
