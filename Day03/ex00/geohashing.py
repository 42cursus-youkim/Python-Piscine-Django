#!/usr/bin/env python3

import sys
import antigravity


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


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 4:
        # args = ["geohashing.py", 37.492118, 127.029925, "2021-05-27-10458.68"]
        args = ["geohashing.py", 37.421542, -122.085589, "2005-05-26-10458.68"]
        terminate(
            "need three parameters - for example try:\npython3 "
            + " ".join(map(str, args)),
        )
    try:
        antigravity.geohash(float(args[1]), float(args[2]), args[3].encode())
    except Exception as e:
        terminate("process input", e)
