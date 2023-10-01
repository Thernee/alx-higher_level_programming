#!/usr/bin/python3

"""Uses requests to fetch 'X-Request-Id' from a passed url"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[i])

    id_val = response.headers.get('X-Request-Id')
    print(id_val)
