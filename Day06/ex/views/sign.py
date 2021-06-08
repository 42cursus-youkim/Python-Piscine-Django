from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

from .view import ScarfView
from ex.forms import SignIn
from django.contrib.auth.forms import UserCreationForm


class Sign(ScarfView):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.info(request, "Signed out")
            return redirect("/ex")
        return super().get(request)

    def post(self, request):
        print(request.POST)
        page = self.pagename(request)

        actions = {
            "signin": self.signin,
            "signup": self.signup,
        }
        if actions.get(page):
            return actions[page](request)
        else:
            raise Exception(f"{page} is invalid!!!!!!")

    def signin(self, request):
        form = SignIn(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if not user:
                messages.error(self.request, "Signin failed; invalid id/pw.")
            else:
                login(self.request, user)
                messages.info(self.request, f"Signed in as {username}.")
                return redirect("/ex")
        return redirect("sign")

    def signup(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            messages.success(request, "Signup successed")
            form.save()

        else:
            messages.error(request, "Signup failed")
            form = UserCreationForm()
        return redirect("sign")
