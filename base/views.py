from django.shortcuts import render
from .models import Product

# Create your views here.

def homePage(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'base/home.html', context)