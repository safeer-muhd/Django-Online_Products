from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from . models import Product

def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})
    #return HttpResponse("<h1>Save The World</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1>")

def contact(request):
    return HttpResponse("<h1>Contact Page</h1>")


