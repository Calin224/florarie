from django.shortcuts import render
from .models import Product, Category

from django.core.paginator import Paginator


# Create your views here.

def homePage(request):
    return render(request, 'base/home.html')


def productsPage(request):
    category = request.GET.get('category')
    if category == None:
        # products = Product.objects.all()[0:3]
        p = Paginator(Product.objects.all(), 2)
        page = request.GET.get('page')
        products_p = p.get_page(page)
        count = Product.objects.all().count()
        page = 'toate'
    else:
        # products = Product.objects.filter(category__name__icontains=category)
        p = Paginator(Product.objects.filter(category__name__icontains=category), 2)
        page = request.GET.get('page')
        products_p = p.get_page(page)
        count = Product.objects.filter(category__name__icontains=category).count()
        page = 'category'

    categories = Category.objects.all()
    context = {'categories': categories, 'products_p': products_p, 'count': count, 'page': page}
    return render(request, 'base/products.html', context)


def productPage(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'base/product.html', context)
