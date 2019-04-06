#!/usr/bin/python3
'''Python script that takes your Github credentials
(username and password) and uses the Github API to display your id'''


def get_github_id(username, password):
    '''Gets github id'''
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    n_dict = r.json()
    print(n_dict.get('id'))


if __name__ == '__main__':
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth
    username = argv[1]
    password = argv[2]
    get_github_id(username, password)
