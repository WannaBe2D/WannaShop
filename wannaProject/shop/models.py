from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='productImage')

    def __str__(self):
        return f'{self.id}'


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image, blank=True, related_name='picProduct')

    def __str__(self):
        return f'ID: {self.id} | {self.name} | {self.category} | {self.price}'
