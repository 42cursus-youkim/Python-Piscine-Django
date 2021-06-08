from django.shortcuts import render
from django.template import loader


def django(request):
    return render(
        request,
        "ex01/django.html",
        {
            "title": "Ex01: Django, framework web.",
            # "src": "https://django-simple-history.readthedocs.io/en/latest/",
        },
    )


def display(request):
    return render(
        request,
        "ex01/display.html",
        {
            "title": "Ex01: Display process of a static page.",
            # "src": "https://en.wikipedia.org/wiki/Django_(web_framework)",
        },
    )


def templates(request):
    return render(
        request,
        "ex01/templates.html",
        {
            "title": "Ex01: Template engine.",
            # "src": "https://www.pluralsight.com/guides/introduction-to-django-templates",
        },
    )
