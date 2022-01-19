from itertools import product
from math import ceil
from typing import ContextManager
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, "customer/index.html", params)


#def login(request):
    #return render(request, "customer/customer_login.html")

#def grains(request):
    #return HttpResponse("<h1>We are at Grains</h1>")

#def vegitables(request):
    #return HttpResponse("<h1>We are at Vegitables</h1>")

def contactus(request):
    return HttpResponse("<h1>We are at Contact Us</h1>")

def aboutus(request):
    return render(request, "customer/aboutus.html")

def tracker(request):
    return HttpResponse("<h1>We are at Tracker</h1>")

def search(request):
    return HttpResponse("<h1>We are at Search</h1>")

def productView(request):
    return HttpResponse("<h1>We are at Product View</h1>")

def checkout(request):
    return HttpResponse("<h1>We are at Checkout</h1>")






