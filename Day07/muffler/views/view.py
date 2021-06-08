from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from django.conf import settings
from django.views.generic import ListView

from django.contrib.auth.forms import UserCreationForm


from muffler.forms import SignIn
from muffler.urls import links
from muffler.enums import PageEnum


def log(line="", desc=""):
    print(f" {desc} ".center(20, "#"))
    print(line)


class ScarfView(ListView):
    context = {
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

    def link_requirements(self, user_authed, links):
        nomap = {
            True: PageEnum.LOG_OUT,
            False: PageEnum.LOG_IN,
        }
        # print(links)
        result = dict()

        for k, v in links.items():
            if v.get("require") != nomap[user_authed]:
                result[k] = v

        # result = filter(links.items)
        # "login": {"require": PageEnum.LOG_OUT},
        return dict(result)

    def begin(self, request):
        user_authed = request.user.is_authenticated
        self.context["links"] = self.link_requirements(user_authed, links)
        if user_authed:
            self.context["username"] = request.user.username
        elif not all(
            [
                request.session.session_key,
                request.session.get("username"),
            ]
        ):
            request.session["username"] = "Anonymous user"
            self.context["username"] = request.session["username"]
            # request.session.set_expiry(42)

        self.context["pagename"] = ScarfView.pagename(request, capital=True)
        # log(request.COOKIES,"cookie")
        # log(request.user,"request.user")
        # log(request.user.is_authenticated,"isauth")
        # log(request.session,"session")
        # log(request.session.session_key,"sessionkey")

    def get(self, request):
        log(request.path)
        log(request.path == "/muffler/")
        if request.path == "/muffler/":
            return redirect("articles")
        self.begin(request)
        # return render(request, f"index.html", self.context)
        return render(
            request, f"{ScarfView.pagename(request)}.html", self.context
        )
