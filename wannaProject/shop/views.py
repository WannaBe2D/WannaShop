from django.shortcuts import render

from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import ProductSerializer
from.models import Product


class ProductList(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

