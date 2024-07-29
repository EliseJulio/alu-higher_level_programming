#!/usr/bin/python3
"""Fetch a url"""

import requests
url = 'https://alu-intranet.hbtn.io/status'

if __name__ == "__main__":
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
