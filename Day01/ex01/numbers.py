#!/usr/bin/env python3


def read_numbers(file_name):
    with open(file_name, "r") as f:
        for n in f.read().split(","):
            print(n.strip())


if __name__ == "__main__":
    read_numbers("numbers.txt")
