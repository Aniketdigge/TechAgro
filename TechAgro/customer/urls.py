from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.index, name="CustomerHomes"),
    path("login/", views.login, name="CustomerLogin"),
]
urlpatterns += staticfiles_urlpatterns()