#!/usr/bin/python3

"""sends a POST request to the passed URL with the email as a parameter"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    email = {"email": argv[2]}
    email = urllib.parse.urlencode(email).encode("utf-8")
    req = urllib.request.Request(argv[1], email)
    with urllib.request.urlopen(req) as response:

        mail = response.read().decode('utf-8')
        print(mail)
