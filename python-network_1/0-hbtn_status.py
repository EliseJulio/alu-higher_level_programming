#!/usr/bin/python3
'''a Python script that fetches a url'''

import urllib.request

url = 'https://alu-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()

    if body == b'OK':
        body = b'Custom status'
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body))
