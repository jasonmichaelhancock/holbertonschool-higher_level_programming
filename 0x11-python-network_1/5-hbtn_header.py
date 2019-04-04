#!/usr/bin/python3
''' displays value of X-Request_Id in response header  '''
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))
