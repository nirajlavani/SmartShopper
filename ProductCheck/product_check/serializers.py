from rest_framework import serializers
from .models import Product

class ProductFileSerializer(serializers.Serializer):
    """
    Serializer used to validate the ProductDetailsAPIView request data.
    """
    file = serializers.FileField()

    class Meta:
        fields = ('file',)


class ProductDetailsSerializer(serializers.Serializer):
    """
    Serializer used to validate the product data.
    """
    product_url = serializers.CharField(max_length=200)
    product_category = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)