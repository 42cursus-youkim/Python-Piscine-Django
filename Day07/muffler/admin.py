from django.contrib import admin
from django.contrib.auth.models import User

from .models import Article, UserFavouriteArticle

admin.site.register(Article)
admin.site.register(UserFavouriteArticle)
