from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
#from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.index, name="CustomerHomes"),
    path("products/", views.products, name="CustomerProduct"),
    path("tracker/", views.tracker, name="CustomerTracker"),
    path("search/", views.search, name="CustomerSearch"),
    path("contactus/", views.contactus, name="CustomerContactUs"),
    path("aboutus/", views.aboutus, name="CustomerAboutUs"),
    path("login/", views.login, name="CustomerLogin"),
    path("signup/", views.signup, name="CustomerSignup"),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)