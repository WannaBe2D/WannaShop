from rest_framework import serializers

from .models import Product, Category, Basket


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category', 'image')

    def get_image(self, product):
        return [str(i.image.url) for i in product.images.all()]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
