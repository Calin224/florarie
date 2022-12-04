from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('products/', views.productsPage, name="products"),
]