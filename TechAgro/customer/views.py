from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    return render(request, "customer/index.html")

#def login(request):
    return render(request, "customer/customer_login.html")

#def grains(request):
    #return HttpResponse("<h1>We are at Grains</h1>")

#def vegitables(request):
    #return HttpResponse("<h1>We are at Vegitables</h1>")

def contactus(request):
    return HttpResponse("<h1>We are at Contact Us</h1>")

def aboutus(request):
    return HttpResponse("<h1>We are at About Us</h1>")

def tracker(request):
    return HttpResponse("<h1>We are at Tracker</h1>")

def search(request):
    return HttpResponse("<h1>We are at Search</h1>")

def productView(request):
    return HttpResponse("<h1>We are at Product View</h1>")

def checkout(request):
    return HttpResponse("<h1>We are at Checkout</h1>")





