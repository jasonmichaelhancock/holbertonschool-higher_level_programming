#!/bin/bash
# Script that takes in a URL, sends parameter, and displays response body.
curl -sL "$1" -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
