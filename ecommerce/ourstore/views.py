from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()[:10] 
    return render(request, "home.html", {"products": products})
