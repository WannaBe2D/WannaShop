from django.shortcuts import render

from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import ProductSerializer, CategorySerializer
from.models import Product, Category


class ProductList(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryList(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
