#!/usr/bin/python3

"""Uses urllib to fetch https://alx-intranet.hbtn.io/status."""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    holder = response.read()
    print(f'Body response:\n\t- type: {type(holder)}')
    print(f'\t- content: {holder}')
    print(f'\t- utf8 content: {holder.decode("utf-8")}')
