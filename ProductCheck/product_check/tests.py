from django.test import TestCase
from .models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(product_url="https://www.amazon.com/", product_category="amazon", is_active=False)
        Product.objects.create(product_url="https://www.walmart.com/", product_category="walmart", is_active=False)

    def test_product_details(self):
        """Created instances are retrieved and respective categories are verified"""
        amazon_product = Product.objects.get(product_url="https://www.amazon.com/")
        walmart_product = Product.objects.get(product_url="https://www.walmart.com/")
        self.assertEqual(amazon_product.product_category, "amazon")
        self.assertEqual(walmart_product.product_category, "walmart")
