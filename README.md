# SmartShopper

### Introduction to SmartShopper

[![IntroVideo](https://i.imgur.com/88ve35a.jpeg)](https://youtu.be/wCpqajHUvOA)

Have you ever bought a product only to find out your friend bought the same product at a cheaper price? Searching for deals can be time-consuming which is why we created SmartShopper, a webapp designed to help users find the cheapest price of their desired product. All users need to do is search for their desired product in the search bar and the webapp outputs the product pricing at various bigbox retailers such as Walmart, Target, and Costco. Our current iteration requests users to upload a .csv file of retailer links to webscrape from and input keywords, via a search bar, to grab relevant information of the desired product. Product information is then displayed back to the user. This document aims to help future developers understand the current foundation of the project and give guidance on how to setup the project locally to improe the webapp further.

Our developments in SmartShopper were achieved using the following technologies: Python3, Django, HTML, CSS, BeautifulSoup (ADD REMAINING TECHNOLOGIES HERE) Any developers who wish to improve Smartshopper should have these technologies installed before proceeding.

### What SmartShopper doing under the hood
![SmartShopperInternals](https://i.imgur.com/SYvKoeA.jpg)

A User looking for a product makes a search via a search bar on the user interface. SmartShopper extracts certain keywords from the search. Using an existing .csv file with links to bigbox retailers like Target and Walmart, the program establishes a connection to these retailer links. The program then webscrapes from the links to find the product's general information (name, description, and price) matching that of the keywords extracted from the user search. Products are then outputted to the user interface for the user to view which retailers provide the cheapest price.

### Goals for the future

* Create Account functionality to save user data and provide more personalized features

* Have SmartShopper have a degree of intelligence and make product recommendations

* Maybe the best price isn't at a bigbox retailer. Create a wider search across a diverse list of stores to find the cheapest price.

### Team Members
