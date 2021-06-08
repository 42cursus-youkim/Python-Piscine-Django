from datetime import datetime
from django.conf import settings


def log(content):
    t = datetime.now().strftime("%b %d %Y %H:%M:%S")
    with open(settings.LOGFILE, "a+") as f:
        f.write(f"{t}  :  {content}\n")


def hist():
    try:
        with open(settings.LOGFILE, "r") as f:
            return f.readlines()
    except IOError as e:
        print(e)
        return []
