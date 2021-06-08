#!/usr/bin/env python3


import sys
import json
import requests
from dewiki.parser import Parser


def terminate(
    message="catastropic failure",
    exception=None,
    endnum=1,
):
    if not exception:
        print(message)
    else:
        print(f"Exception\n{exception}\noccured while trying to {message}")
    sys.exit(endnum)


def check_args(args):
    if len(args) != 2:
        terminate(
            "needs single file argument to search but given "
            + str(len(args) - 1)
        )


def get_article(name):
    page_url = (
        "https://en.wikipedia.org/w/"
        "api.php?action=query"
        f"&titles={name}"
        "&prop=revisions"
        "&rvprop=content"
        "&format=json"
    )
    request = requests.get(page_url)

    if not request or request.status_code != 200:
        terminate("connection failed with result " + str(request.status_code))

    if not request.text:
        terminate(
            f"failed to fetch text, maybe article {name} not in wikipedia"
        )

    return json.loads(request.text)["query"]["pages"]


def parse(raw_page):
    for page_id in raw_page.keys():
        for k in raw_page[page_id].keys():
            if k == "revisions":
                raw_page_recent = raw_page[page_id][k][0]
                break
    try:
        mid_page = raw_page_recent[r"*"]
        return Parser().parse_string(mid_page)
    except Exception as e:
        terminate(f"parce text starting with {str(raw_page_recent)[:50]}...", e)


def write(name, page):
    name = f"{name}.wiki"
    try:
        with open(name, "w") as f:
            f.write(page)
    except Exception as e:
        terminate(f"write {name}", e)


def wiki():
    check_args(sys.argv)
    name = sys.argv[1]
    write(name, parse(get_article(name)))


if __name__ == "__main__":
    wiki()
