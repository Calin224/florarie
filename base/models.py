from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    resume = models.TextField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=10)
    price = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
