from django.contrib import admin

from .models import Category, Product, Image


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    pass
