#!/usr/bin/python3
""" A script that sends a request to a given
URL and displays the response body.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    rquest = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(rquest) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as ex:
        print("Error code: {}".format(ex.code))
