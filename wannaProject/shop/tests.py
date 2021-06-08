from django.test import TestCase
from rest_framework.test import APITestCase

from .models import Product, Category
from .serializers import ProductSerializer


class ApiTests(APITestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name='category1')
        self.category2 = Category.objects.create(name='category2')

    def test_product(self):
        self.product1 = Product.objects.create(name='product1',
                                               description='des',
                                               price='134.35',
                                               category=self.category1)

        self.product2 = Product.objects.create(name='product2',
                                               description='des',
                                               price='15.55',
                                               category=self.category2)

        data = ProductSerializer([self.product1, self.product2], many=True).data

        expensed_data = [
            {
                'name': 'product1',
                'description': 'des',
                'price': '134.35',
                'category': 1,
                'image': [],
            },
            {
                'name': 'product2',
                'description': 'des',
                'price': '15.55',
                'category': 2,
                'image': [],
            },
        ]

        self.assertEqual(expensed_data, data)
