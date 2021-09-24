from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.ProductDetailsAPIView.as_view(), name='product-details'),
]


