#!/usr/bin/python3
""" A script that displays the X-Request-Id header variable
of a request to a given URL.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    rquest = urllib.request.Request(url)
    with urllib.request.urlopen(rquest) as response:
        print(dict(response.headers).get("X-Request-Id"))
