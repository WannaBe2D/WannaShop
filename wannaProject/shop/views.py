from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import ProductSerializer, CategorySerializer, ProductCategoryDetailSerializer, OrderSerializer
from .models import Product, Category, Basket, Order


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

    permission_classes = [IsAuthenticated]


class ProductList(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


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
                             ({"id": i.id, "name": i.name, "price": i.price, "image": {str(i.image.url) for i in i.images.all()}} for i in items),
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


class MyOrder(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Order.objects.filter(owner=request.user)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Order.objects.filter(owner=request.user)
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def add_to_order(request):
    items = Basket.objects.get(owner=request.user).items.all()
    if items:
        order = Order.objects.create(owner=request.user)
        order.items.set(items)
        Basket.objects.get(owner=request.user).items.clear()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)