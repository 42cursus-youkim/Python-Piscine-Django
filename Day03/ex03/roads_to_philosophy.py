#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup


def terminate(message="catastropic failure", exception=None, endnum=1):
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


def filtering(tag):
    return not (tag is None or tag.has_attr("role")) and tag.name == "a"


def is_link_valid(link):
    nolst = [
        "#",
        "/wiki/File",
        "/wiki/Help",
        "/wikipedia:",
        "/wiki/Wikipedia:Citation_needed",
        "//upload.wikimedia.org/",
        "//commons.wikimedia.org/",
    ]
    for n in nolst:
        if link.startswith(n):
            return False
    return link.startswith("/wiki/")


def get_html(name):
    url = f"https://en.wikipedia.org/wiki/{name}"
    request = requests.get(url)

    if not request or request.status_code != 200:
        terminate("connection failed with result " + str(request.status_code))
    soup = BeautifulSoup(request.text, "html.parser")
    return soup


def search_html(soup):
    for a in [
        {"id": "bodyContent"},
        {"id": "mw-content-text"},
        {"class": "mw-parser-output"},
    ]:
        soup = soup.find("div", attrs=a)

    for child in soup.children:
        if child.name == "p":
            for a in child.find_all(filtering):
                link = str(a.get("href"))
                if is_link_valid(link):
                    # print(link.replace("/wiki/", "").replace(" ", "_"))
                    return link.replace("/wiki/", "").replace(" ", "_")


def crawl():
    check_args(sys.argv)
    name = sys.argv[1].replace(" ", "_")
    visited = list()

    while True:
        if name == "Philosophy":
            terminate(
                f"{name}\n"
                f"{len(visited)} roads from "
                f"{visited[0] if len(visited) else name} to {name} !"
            )

        print(name)
        name = search_html(get_html(name))

        if name in visited:
            terminate(f"{name}\nIt leads to an infinite loop !")

        visited.append(name) if name else terminate("It's a dead end !")


if __name__ == "__main__":
    crawl()
