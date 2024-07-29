#!/usr/bin/python3
"""Fetch a url"""

# File path: fetch_status.py

import requests

def fetch_status(url):
    with requests.get(url) as response:
        if url == 'https://alu-intranet.hbtn.io/status':
            body = response.text
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
        elif url == 'http://0.0.0.0:5050/status':
            body = response.content
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
