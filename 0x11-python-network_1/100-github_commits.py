#!/usr/bin/python3
""" ./script.py <repo name> <repo owner> """

import sys
import requests


def main():
    """ def aut"""
    owner = sys.argv[1]
    repo = sys.argv[2]
    limit = 10
    url = f'https://api.github.com/repos\
/{repo}/{owner}/commits?per_page={limit}'

    res = requests.get(url).json()
    for c in res:
        name = c.get("commit").get("author").get("name")
        print(f'{c.get("sha")}: {name}')


if __name__ == "__main__":
    main()
