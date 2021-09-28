from django.shortcuts import render
from django.http import HttpResponse
from . import models as web


i = 1;
image_url = [];
product_price = [];
product_url =[];

# Create your views here.

def home(request):
    return render(request,'home.html')


def result_page(request): 
    image_url, product_price, product_url = web.csv_cfile();
    return render(request,"result_page.html",{'image_link1' : image_url[0],'p_price1' :product_price[0],'p_url1' :product_url[0],'image_link2' : image_url[1],'p_price2' :product_price[1],'p_url2' :product_url[1],'image_link3' : image_url[2],'p_price3' :product_price[2],'p_url3' :product_url[2],'image_link4' : image_url[3],'p_price4' :product_price[3],'p_url4' :product_url[3],'image_link5' : image_url[4],'p_price5' :product_price[4],'p_url5' :product_url[4],'image_link6' : image_url[5],'p_price6' :product_price[5],'p_url6' :product_url[5],'image_link7' : image_url[6],'p_price7' :product_price[6],'p_url7' :product_url[6],'image_link8' : image_url[7],'p_price8' :product_price[7],'p_url8' :product_url[7]})