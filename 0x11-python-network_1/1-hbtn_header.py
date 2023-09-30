#!/usr/bin/python3

"""Uses urllib to fetch https://alx-intranet.hbtn.io/status."""
import urllib.request
from sys import argv

with urllib.request.urlopen(argv[1]) as response:

    id_val = response.headers.get('X-Request-Id')
    print(id_val)
