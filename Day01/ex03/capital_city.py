#!/usr/bin/env python3


import sys


def merge_dict(first, last):
    return dict((k, last[v]) for k, v in first.items())


def search():
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO",
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver",
    }
    if len(sys.argv) == 2:
        new_dict = merge_dict(states, capital_cities)
        q = sys.argv[1]
        print(new_dict.get(q) or "Unknown State")


if __name__ == "__main__":
    search()
