from django.urls import path  , include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from . import views
urlpatterns = [
    path('panel/' , views.panel),
    path('' , views.home),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

