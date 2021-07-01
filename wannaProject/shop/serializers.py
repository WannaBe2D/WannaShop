from rest_framework import serializers

from .models import Product, Category, Basket, Order


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'sex', 'description', 'price', 'category', 'image')

    def get_image(self, product):
        return [str(i.image.url) for i in product.images.all()]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductCategoryDetailSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    @staticmethod
    def get_products(obj):
        return ProductSerializer(Product.objects.filter(category=obj), many=True).data


class OrderSerializer(serializers.ModelSerializer):
    items = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ('id', 'items',)
