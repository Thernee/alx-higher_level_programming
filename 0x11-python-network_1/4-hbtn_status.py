#!/usr/bin/python3

"""Uses requets to fetch https://alx-intranet.hbtn.io/status. and print it"""
import requests

if __name__ == "__main__":
    holder = requests.get('https://alx-intranet.hbtn.io/status')
    print(f'Body response:\n\t- type: {type(holder.text)}')
    print(f'\t- content: {holder.text}')
