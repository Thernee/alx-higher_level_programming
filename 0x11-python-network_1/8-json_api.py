#!/usr/bin/python3

"""sends request to a URL and displays body of the response, or error"""
import requests
from sys import argv

if __name__ == "__main__":
    if argv[1]:
        q = {'q': argv[1]}
    else:
        q = {'q': ""}
    req = requests.post('http://0.0.0.0:5000/search_user', data=q)
    try:
        jason_dict = req.json()
        if json_dict:
            print(f"[{json_dict['id']}] {json_dict['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
