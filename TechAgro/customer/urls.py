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
    #path("login/", views.login, name="CustomerLogin"),
    #path("grains/", views.grains, name="CustomerGrains"),
    #path("vegitables/", views.vegitables, name="CustomerVegitables"),
    path("contactus/", views.contactus, name="ContactUs"),
    path("aboutus/", views.aboutus, name="AboutUs"),
    path("tracker/", views.tracker, name="Tracker"),
    path("search/", views.search, name="Search"),
    path("productView/", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="CheckOut"),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)