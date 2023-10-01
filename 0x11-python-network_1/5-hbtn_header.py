#!/usr/bin/python3

"""Uses requests to fetch 'X-Request-Id' from a passed url"""
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])

    id_val = req.headers.get('X-Request-Id')
    print(id_val)
