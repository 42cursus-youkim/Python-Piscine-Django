from django.conf.urls import url
from django.urls import path
from .links import general, signs
from . import views

urlpatterns = [
    path(link, views.ScarfView.as_view(), name=link) for link in general
]

for link in signs:
    urlpatterns.append(path(link, views.Sign.as_view(), name=link))
