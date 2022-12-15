from django.shortcuts import render
from django.template.loader import get_template

from .models import Product, Category

from django.core.paginator import Paginator
from django.core.mail import send_mail, EmailMultiAlternatives


# Create your views here.

def homePage(request):
    return render(request, 'base/home.html')


def productsPage(request):
    category = request.GET.get('category')
    if category == None:
        # products = Product.objects.all()[0:3]
        p = Paginator(Product.objects.all(), 6)
        page = request.GET.get('page')
        products_p = p.get_page(page)
        count = Product.objects.all().count()
        page = 'toate'
    else:
        products_p = Product.objects.filter(category__name__icontains=category)
        # p = Paginator(Product.objects.filter(category__name__icontains=category), 2)
        # page = request.GET.get('page')
        # products_p = p.get_page(page)
        # count = Product.objects.filter(category__name__icontains=category).count()
        count = products_p.count()
        page = 'category'


    categories = Category.objects.all()
    context = {'categories': categories, 'products_p': products_p, 'count': count, 'page': page, 'category': category}
    return render(request, 'base/products.html', context)


def productPage(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'base/product.html', context)


def contactPage(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        files = request.FILES.getlist('files')

        context_data = {'name': name, 'email': email, 'subject': subject, 'message': message, 'files': files}

        print(files)

        html_content = get_template('base/email.html').render(context_data)

        msg = EmailMultiAlternatives(subject, message, email, ['sanducalinm@gmail.com'])
        msg.attach_alternative(html_content, "text/html")
        for f in files:
            msg.attach(f.name, f.read(), f.content_type)
        msg.send()

    context = {}
    return render(request, 'base/contact.html', context)
