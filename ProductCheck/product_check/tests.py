import csv
from django.test import TestCase
from .models import Product
from .product_scraping import AmazonScrapper, WalmartScrapper, TargetScrapper, CostcoScrapper
from .views import scraping_class


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

    def test_product_details_post(self):
        test_file = open('product_check/test_data/test_data.csv', 'r')
        response = self.client.post('/product_check/details/', {'file': test_file})
        self.assertEqual(response.status_code, 200)

    def test_amazon_scrapper(self):
        test_file = csv.DictReader(open('product_check/test_data/amazon_test_data.csv', 'r'))
        for row in test_file:
            scrapper = scraping_class[row['product_category']](row['product_url'])
            data = scrapper.fetch_product_details()
            self.assertEqual(data.get('product_url'), row['product_url'])

    def test_walmart_scrapper(self):
        test_file = csv.DictReader(open('product_check/test_data/walmart_test_data.csv', 'r'))
        for row in test_file:
            scrapper = scraping_class[row['product_category']](row['product_url'])
            data = scrapper.fetch_product_details()
            self.assertEqual(data.get('product_url'), row['product_url'])