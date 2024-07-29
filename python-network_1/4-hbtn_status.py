#!/usr/bin/python3
"""Fetch a url"""

import requests

url = 'https://alu-intranet.hbtn.io/status'

response = requests.get(url)
body = response.text

if body.strip() == "OK":
    body = "Custom status"
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
