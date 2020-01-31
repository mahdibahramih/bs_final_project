from django.urls import path  , include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from . import views
urlpatterns = [
    path('' , views.home),
]

