#!/usr/bin/env python3

from path import Path  # type: ignore

if __name__ == "__main__":
    temp = Path(".") / "temp"
    if not temp.isdir():
        temp.mkdir()
    f = temp / "test.txt"
    if not f.isfile():
        f.touch()
    f.write_text("pypy")
    for l in f.lines():
        print(l)
