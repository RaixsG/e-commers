from django.db import models
from users.models import User

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(default='/placeholder.png', null=True)
    category = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=100, blank=True)
    rating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    count_in_stock = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

class Reviews(models.Model):
    products = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)