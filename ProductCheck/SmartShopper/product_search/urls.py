from django.urls import path 

from . import views

urlpatterns = [path('',views.home, name='home'), path('result_page',views.result_page, name='result_page')]