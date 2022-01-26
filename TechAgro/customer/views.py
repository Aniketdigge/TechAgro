from itertools import product
from math import ceil
from typing import ContextManager
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    return render(request, "customer/index.html")

def products(request):
    return render(request, "customer/customer_product.html")

def tracker(request):
    return render(request, "customer/customer_tracker.html")

def search(request):
    return render(request, "customer/customer_search.html")

def contactus(request):
    return render(request, "customer/customer_contactus.html")

def aboutus(request):
    return render(request, "customer/customer_aboutus.html")

def login(request):
    return render(request, "customer/customer_login.html")

def signup(request):
    return render(request, "customer/customer_signup.html")






