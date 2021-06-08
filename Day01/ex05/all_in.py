#!/usr/bin/env python3


import sys


def cut(arg):
    return [a.strip() for a in arg.split(",") if a.strip()]


def rev(dct):
    return dict((v, k) for k, v in dct.items())


def merge_dict(first, last):
    return dict((k, last.get(v)) for k, v in first.items())


def get_nocase(key, dct):
    dct = dict((k.casefold(), v) for k, v in dct.items())
    return dct.get(key.casefold())


def search_dict(qd, kv, vk):
    for name, q in qd.items():
        if get_nocase(q, kv):
            print(get_nocase(q, kv), "is the capital of", q)
        elif get_nocase(q, vk):
            print(q, "is the capital of", get_nocase(q, vk))
        else:
            print(name, "is neither a capital city nor a state")


def search_all():
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
        arg = cut(sys.argv[1])
        qdict = dict(zip(arg, list(map(str.title, arg))))
        state_cap = merge_dict(states, capital_cities)
        search_dict(qdict, state_cap, rev(state_cap))


if __name__ == "__main__":
    search_all()
