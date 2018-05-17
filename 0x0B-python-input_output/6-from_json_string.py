#!/usr/bin/python3
import json
def from_json_string(my_str):
    return json.JSONDecoder().decode(my_str)
