#!/usr/bin/python3
"""Fetch a url"""

# File path: fetch_status.py

import requests

url = 'https://alu-intranet.hbtn.io/status'

with requests.get(url) as response:
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
