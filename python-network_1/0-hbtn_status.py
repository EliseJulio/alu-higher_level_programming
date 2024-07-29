#!/usr/bin/python3
'''a Python script that fetches a url'''

# File path: fetch_status.py

import urllib.request

url = 'https://alu-intranet.hbtn.io/status'

if __name__ == '__main__':
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
