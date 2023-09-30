#!/usr/bin/python3

"""Uses urllib to fetch https://alx-intranet.hbtn.io/status."""
import urllib.request
from sys import argv

if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:

        id_val = response.headers.get('X-Request-Id')
        print(id_val)
