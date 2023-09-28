#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response in bytes
# You have to use curl

# Check if the user provided a URL as an argument
curl -sw '%{size_download}\n' -o /dev/null "$1"
