from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.index, name="CustomerHomes"),
]
urlpatterns += staticfiles_urlpatterns()