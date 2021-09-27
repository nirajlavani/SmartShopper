from django.db import models
from django.utils import timezone


class Product(models.Model):
    """
    Model used for storing scrapped product data along with creation and modified times.
    """
    product_name = models.CharField(max_length=100, null=True, blank=True)
    product_url = models.URLField(max_length=200, null=False, blank=False)
    product_category = models.CharField(max_length=20, null=True, blank=True)
    product_price = models.FloatField(default=None, null=True, blank=True)
    product_review_score = models.CharField(max_length=20, null=True, blank=True)
    product_availability = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
