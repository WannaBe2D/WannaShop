from rest_framework import serializers

from.models import Product


class ProductSerializer(serializers.ModelSerializer):
    im = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category', 'im')

    def get_im(self, product):
        images = product.images.all()
        m = [str(i.image.url) for i in images]
        return m