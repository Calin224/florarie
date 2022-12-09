from django.shortcuts import render
from .models import Product, Category


# Create your views here.

def homePage(request):
    return render(request, 'base/home.html')


def productsPage(request):
    category = request.GET.get('category')
    if category == None:
        products = Product.objects.all()[0:3]
    else:
        products = Product.objects.filter(category__name__icontains=category)

    categories = Category.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'base/products.html', context)


def productPage(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'base/product.html', context)
