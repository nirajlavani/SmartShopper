[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://app.travis-ci.com/chandur626/SmartShopper.svg?branch=main)](https://app.travis-ci.com/chandur626/SmartShopper)
[![Build Status - GitHub](https://github.com/chandur626/SmartShopper/actions/workflows/django.yml/badge.svg)](https://github.com/chandur626/SmartShopper/actions/workflows/django.yml)
![Github](https://img.shields.io/badge/language-python-blue.svg)
[![Coverage Status](https://coveralls.io/repos/github/chandur626/SmartShopper/badge.svg?branch=main)](https://coveralls.io/github/chandur626/SmartShopper?branch=main)

# SmartShopper

https://user-images.githubusercontent.com/60410421/135014006-921089ab-d598-4672-85d1-bd461d1863a5.mp4

### Introduction to SmartShopper
Have you ever bought a product only to find out your friend bought the same product at a cheaper price? 

Searching for deals can be time-consuming which is why we created SmartShopper, a webapp designed to help users find the cheapest price of their desired product. All users need to do is search for their desired product in the search bar and the webapp outputs the product pricing at various bigbox retailers such as Walmart, Target, and Costco. Our current iteration requests users to upload a .csv file of retailer links to webscrape from and input keywords, via a search bar, to grab relevant information of the desired product. Product information is then displayed back to the user. This document aims to help future developers understand the current foundation of the project and give guidance on how to setup the project locally to improe the webapp further.

Our developments in SmartShopper were achieved using the following technologies: Python3, Django, HTML, and CSS. Any developers who wish to improve Smartshopper should have these technologies installed before proceeding.

### What SmartShopper is doing under the hood
![SmartShopperInternals](https://i.imgur.com/SYvKoeA.jpg)

A User looking for a product makes a search via a search bar on the user interface. SmartShopper extracts certain keywords from the search. Using an existing .csv file with links to bigbox retailers like Target and Walmart, the program establishes a connection to these retailer links. The program then webscrapes from the links to find the product's general information (name, description, and price) matching that of the keywords extracted from the user search. Products are then outputted to the user interface for the user to view which retailers provide the cheapest price.

### QuickStart
---
<br/> Clone the repository and go to the directory
```
git clone https://github.com/chandur626/SmartShopper.git
```
<br/> Install the required packages
```
pip install -r requirements.txt
```
<br/> Start the server my following command
```
cd ProductCheck
python manage.py runserver
```
<br/> You could see the server running at http://127.0.0.1:8000/

<br/> To check everything is working correct run the tests by using the following command.
```
python manage.py test
```

<br/> Start the cron job by running the following command.
```
python manage.py crontab add
```

<br/> To stop the cron job, run the following command.
```
python manage.py crontab remove
```

<br/> To stop the cron job, run the following command.
```
python manage.py crontab remove
```

<br/> Run the following command to make sure that the cron jobs are initiated.
```
crontab -l
```


### Goals for the future

* Create Account functionality to save user data and provide more personalized features

* Have SmartShopper have a degree of intelligence and make product recommendations

* Maybe the best price isn't at a bigbox retailer. Create a wider search across a diverse list of stores to find the cheapest price.

* Checkout project board for other enhancements.

### Team Members
[Chandrahas Reddy Mandapati](https://github.com/chandur626)

[Sri Pallavi Damuluri](https://github.com/SriPallaviDamuluri)

[Niraj Lavani](https://github.com/nirajlavani)

[Harini Bharata](https://github.com/HariniBharata)

[Sandesh Aladhalli Shivarudre Gowda](https://github.com/05sandesh)
