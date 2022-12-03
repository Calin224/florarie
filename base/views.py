from django.shortcuts import render
from .models import Product

# Create your views here.

def homePage(request):

    return render(request, 'base/home.html')