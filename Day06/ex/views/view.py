from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from django.conf import settings
from django.views.generic import View, FormView

from django.contrib.auth.forms import UserCreationForm


from ex.forms import SignIn
from ex.links import links

import random


def log(desc="", line=""):
    print(f" {desc} ".center(20, "#"))
    print(line)


class ScarfView(View):
    context = {
        "links": links,
        "signin": SignIn(),
        "signup": UserCreationForm(),
    }

    @staticmethod
    def pagename(request, capital=False, setdefault=True):
        pagename = request.path.split("/")[-1]
        if setdefault:
            pagename = pagename or "index"
        if capital:
            pagename = pagename.capitalize()
        return pagename

    def begin(self, request):
        if request.user.is_authenticated:
            self.context["username"] = request.user.username
        elif not all(
            [
                request.session.session_key,
                request.session.get("username"),
            ]
        ):
            request.session["username"] = random.choice(settings.NAMES)
            self.context["username"] = request.session["username"]
            request.session.set_expiry(42)

        self.context["pagename"] = ScarfView.pagename(request, capital=True)
        # log("cookie", request.COOKIES)
        # log("request.user", request.user)
        # log("isauth", request.user.is_authenticated)
        # log("session", request.session)
        # log("sessionkey", request.session.session_key)

    def get(self, request):
        self.begin(request)
        # return render(request, f"index.html", self.context)
        return render(
            request, f"{ScarfView.pagename(request)}.html", self.context
        )
