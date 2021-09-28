from django.db import models
import csv

image_url = [];
product_price = [];
product_url =[];


def csv_cfile():

    with open(r"C:\Users\mailt\SE_project\SmartShopper\product_search\web_data.csv",'r') as csv_file:
        csv_reader= csv.reader(csv_file)    
        
        next(csv_reader)
        for line in csv_reader:
            image_url.append(line[0])
            product_price.append(line[1])
            product_url.append(line[2])
    return image_url, product_price , product_url


csv_cfile();

print(product_price)






   


# Create your models here.
