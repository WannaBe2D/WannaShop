from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass
