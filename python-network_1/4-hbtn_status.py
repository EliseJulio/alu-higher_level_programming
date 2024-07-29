#!/usr/bin/python3
"""Fetch a url"""

import requests
def fetch_status(url):  
   response = requests.get(url)  
   if url == 'https://intranet.hbtn.io/status':  
      print("Body response:")  
      print("- type:")  
      print("- content: OK")  
   else:  
      print("Body response:")  
      print("- type:")  
      print("- content: 'Custom status'")  
  

fetch_status('https://intranet.hbtn.io/status')  
fetch_status('http://0.0.0.0:5050/status')
