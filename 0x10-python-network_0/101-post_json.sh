#!/bin/bash
#  a script sends a JSON POST request to a given URL with a given filei's json.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
