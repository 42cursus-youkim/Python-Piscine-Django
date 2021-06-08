from django.conf.urls import url
from django.urls import path

from muffler.enums import PageEnum

links = {
    "articles": {},
    "login": {"require": PageEnum.LOG_OUT},
    "register": {"require": PageEnum.LOG_OUT},
    "logout": {"require": PageEnum.LOG_IN},
}

import muffler.views as views  # to deal with circular dependancy

linkviews = {
    "articles": views.ArticleView,
    "login": views.SignView,
    "register": views.SignView,
    "logout": views.SignView,
}

mergedlinks = {
    k: {
        "name": k,
        "require": p.get("require", PageEnum.LOG_ANY),
        "class": linkviews.get(k, views.ScarfView),
    }
    for k, p in links.items()
}

urlpatterns = [
    path(act["name"], act["class"].as_view(), name=act["name"])
    for l, act in mergedlinks.items()
]

urlpatterns.append(path("", views.ScarfView.as_view(), name="root"))

# for link in signs:
#     #link = link or "default"
#     urlpatterns.append(path(link, views.Sign.as_view(), name=link))

"""
TODO:
ex00: *generic views*
    Articles
    Home
    Login
ex01: *generic views*
    Publications
    Detail
    Logout
    Favorites
ex02: *CreateView*
    Register
    Publish
    Add to favourite
"""
