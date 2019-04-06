#!/usr/bin/python3
'''  sends a request to passed URL and displays response  '''
import urllib.request as request
import urllib.error as error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))