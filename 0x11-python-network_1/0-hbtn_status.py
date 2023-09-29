#!/usr/bin/python3
"""A script that fetches https://intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as res_ponse:
        bdy = res_ponse.read()
        print("Body response:")
        print("\t- type: {}".format(type(bdy)))
        print("\t- content: {}".format(bdy))
        print("\t- utf8 content: {}".format(bdy.decode("utf-8")))
