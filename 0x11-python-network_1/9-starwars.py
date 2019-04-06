#!/usr/bin/python3
''' searches for a string in the star wars api  '''
import requests
from sys import argv


if __name__ == "__main__":
    params = {'search': argv[1]}
    url = "https://swapi.co/api/people"
    req = requests.get(url, params=params)
    people = req.json()
    print("Number of results: {}".format(people.get('count')))
    for person in people.get('results'):
        print(person.get('name'))
