from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import ProductSerializer, CategorySerializer, ProductCategoryDetailSerializer
from .models import Product, Category, Basket


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

    permission_classes = [IsAuthenticated]


class ProductList(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryList(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    action_to_serializer = {
        "retrieve": ProductCategoryDetailSerializer,
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class MyBasket(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        if not hasattr(request.user, 'basket'):
            Basket.objects.create(owner=request.user)

        items = request.user.basket.items.all()
        return Response({"products":
                             ({"id": i.id, "name": i.name, "price": i.price} for i in items),
                         "totalPrice":
                             (i.price for i in items)})


class AddProductInBasket(APIView):
    permission_classes = [IsAuthenticated]

    parser_classes = [JSONParser]

    def post(self, request, format=None):
        if not hasattr(request.user, 'basket'):
            Basket.objects.create(owner=request.user)

        product = Product.objects.get(id=request.data['id'])
        basket = Basket.objects.get(owner_id=request.user.id)
        basket.items.add(product)
        basket.save()
        return Response(status=status.HTTP_200_OK)
