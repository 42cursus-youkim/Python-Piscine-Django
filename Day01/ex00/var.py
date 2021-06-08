#!/usr/bin/env python3


def my_var():
    varlst = [42, "42", "fourty-two", 42.0, True, [42], {42: 42}, (42,), set()]
    for x in varlst:
        print(x, "has a type", type(x))


if __name__ == "__main__":
    my_var()
