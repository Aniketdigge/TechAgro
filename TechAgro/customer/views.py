from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "customer/index.html")

def login(request):
    return render(request, "customer/customer_login.html")

def grains(request):
    return HttpResponse("<h1>We are at Grains</h1>")

def vegitables(request):
    return HttpResponse("<h1>We are at Vegitables</h1>")

def contactus(request):
    return HttpResponse("<h1>We are at Contact Us</h1>")

def aboutus(request):
    return HttpResponse("<h1>We are at About Us</h1>")



