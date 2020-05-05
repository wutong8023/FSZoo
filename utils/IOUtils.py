"""
basic functions for IO.

Author: Tong
Time: 04-05-2020
"""
import json
import os

__all__ = [
    "check_path"
]


def check_path(dir):
    if os.path.exists(dir):
        print('Found: ', dir)
        return
    else:
        os.mkdir(dir)
        print(dir, " has been created.")
