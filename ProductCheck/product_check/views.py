import io
import csv

from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ProductDetailsSerializer
from .product_scraping import AmazonScrapper, WalmartScrapper, TargetScrapper, CostcoScrapper
from rest_framework.generics import CreateAPIView

scraping_class = {
    'amazon': AmazonScrapper,
    'walmart': WalmartScrapper,
    'target': TargetScrapper,
    'costco': CostcoScrapper,
}


class ProductDetailsAPIView(CreateAPIView):
    serializer_class = ProductDetailsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.DictReader(io_string)
        data = []
        for row in reader:
            scrapper = scraping_class[row['code']](row['url'])
            data.append(scrapper.fetch_product_details())
        return Response(status=status.HTTP_200_OK, data=data)
