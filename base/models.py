from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    resume = models.TextField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=10)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name