from django.shortcuts import render
from .form import ScarfForm
from .utils import hist, log
from django.http import HttpResponseRedirect


def main(request):
    return render(
        request,
        "ex02/index.html",
        {
            "form": ScarfForm(),
            "history": hist(),
        },
    )


def post(request):
    if request.method == "POST":
        if ScarfForm(request.POST).is_valid():
            log(request.POST.get("content"))
        return HttpResponseRedirect("/ex02")
