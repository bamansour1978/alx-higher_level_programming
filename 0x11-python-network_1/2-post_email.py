#!/usr/bin/python3
"""A script that sends a POST request to a given URL with a given email.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    dic = urllib.parse.urlencode(email).encode("ascii")

    rquest = urllib.request.Request(url, dic)
    with urllib.request.urlopen(rquest) as response:
        print(response.read().decode("utf-8"))
