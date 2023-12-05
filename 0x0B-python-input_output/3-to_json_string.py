#!/usr/bin/python3
"""Define to_json_string module """

import json

def to_json_string(my_obj):
    """
    returns JSON representation of an object (string)
    """

    return json.dums(my_obj)
