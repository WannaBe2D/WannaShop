from django.contrib import admin

from .models import Category, Product, Image, Basket, Order


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    pass


@admin.register(Basket)
class BasketImage(admin.ModelAdmin):
    pass


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    pass
