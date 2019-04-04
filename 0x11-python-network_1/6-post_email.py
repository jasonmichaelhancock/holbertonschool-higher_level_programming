#!/usr/bin/python3
'''  sends a POST request to passed URL and displays response  '''
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    data = {'email': argv[2]}
    r = requests.post(url, data)
    print(r.text)
