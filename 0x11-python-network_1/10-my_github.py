#!/usr/bin/python3

"""Takes Github credentials and give id"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    credentials = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get('https://api.github.com/user', auth=credentials)
    try:
        json_dict = req.json()
        print(f"{json_dict.get('id')}")
    except ValueError:
        pass
