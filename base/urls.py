from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('products/', views.productsPage, name="products"),
    path('product/<str:pk>', views.productPage, name="product"),
    path('/contact', views.contactPage, name="contact")
]