#!/usr/bin/python3
"""./9-script.py <search string>
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://swapi.co/api/people"
    parms = {"search": sys.argv[1]}
    reslts = requests.get(url, params=parms).json()

    print("Number of results: {}".format(reslts.get("count")))
    [print(r.get("name")) for r in reslts.get("results")]
