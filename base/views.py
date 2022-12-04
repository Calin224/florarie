from django.shortcuts import render
from .models import Product


# Create your views here.

def homePage(request):
    return render(request, 'base/home.html')


def productsPage(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'base/products.html', context)
