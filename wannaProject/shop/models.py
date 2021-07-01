from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'


class Image(models.Model):
    image = models.ImageField(upload_to='productImage')

    def __str__(self):
        return f'{self.id} {self.image}'


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image, blank=True, related_name='picProduct')
    SEX_CHOICES = [
        ('M', 'MEN'),
        ('W', 'WOMEN'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M')

    def __str__(self):
        return f'ID: {self.id} | {self.name} | {self.category} | {self.price}'


class Basket(models.Model):
    items = models.ManyToManyField(Product, blank=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.owner.id} | {self.owner}'


class Order(models.Model):
    items = models.ManyToManyField(Product)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} | {self.owner}'
