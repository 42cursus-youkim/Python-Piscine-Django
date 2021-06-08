#!/usr/bin/env python3


import re
import os
import sys

import settings  # noqa: used by module_vars


def module_vars(module_name):
    module = globals().get(module_name)
    if module:
        module_items = module.__dict__.items()
        return dict((k, v) for k, v in module_items if "_" not in k)
    return None


def file_task(file_name, operation="r", towrite=None, ex=None):
    if (operation == "w") or os.path.isfile(file_name):
        with open(file_name, operation) as f:
            if (not ex) or (ex and re.search(ex, file_name)):
                if operation == "r":
                    return f.read()
                elif operation == "w" and towrite:
                    return f.write(towrite)
    raise ValueError


def apply_info(lines, info):
    try:
        return lines.format_map(info)
    except Exception:
        return lines.format(**info)


def render_html(html_file):
    args = sys.argv
    if len(args) == 2:
        info = module_vars("settings")
        html = file_task(args[1], ex=".template")
        file_task(html_file, "w", apply_info(html, info))
    else:
        raise ValueError("expected 2 arguments but recieved " + str(len(args)))


if __name__ == "__main__":
    render_html("myCV.html")
