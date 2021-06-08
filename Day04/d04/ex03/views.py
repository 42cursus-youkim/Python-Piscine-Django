from django.shortcuts import render


def index(request):
    return render(request, "ex03/index.html", {"rows": range(0, 255, 5)})
