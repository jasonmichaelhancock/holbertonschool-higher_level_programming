#!/bin/bash
# Script that takes in a URL, sends parameter, and displays response body.
curl -sL "$1" -H "X-HolbertonSchool-User-Id: 98"
