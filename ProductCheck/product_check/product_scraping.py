import json
from selenium import webdriver
from bs4 import BeautifulSoup

from django.conf import settings


class AmazonScrapper:
    """
    Responsible for scrapping amazon data.
    """
    def __init__(self, url):
        self.product_url = url
        self.product_name = None
        self.product_price = None
        self.product_review_score = None
        self.product_availability = None

    def parse_page_content(self, soup):
        try:
            self.product_name = soup.find(id='productTitle').get_text().strip()
        except Exception as e:
            self.product_name = 'BAD REQUEST'
        try:
            self.product_price = soup.find('span', {"id": "priceblock_ourprice"})
            if self.product_price:
                self.product_price = float(self.product_price.get_text().replace('$', '').replace(',', '').strip())
            else:
                self.product_price = soup.find('span', {"id": "priceblock_dealprice"})
                self.product_price = float(self.product_price.get_text().replace('$', '').replace(',', '').strip())
        except Exception as e:
            self.product_price = 'BAD REQUEST'
        try:
            self.product_review_score = soup.find('span', {"class": "a-icon-alt"}).get_text()
        except Exception as e:
            self.product_review_score = 'BAD REQUEST'
        try:
            soup.select('#availability .a-color-state')[0].get_text().strip()
            self.product_availability = 'Out of Stock'
        except:
            self.product_availability = 'Available'

    def fetch_product_details(self):
        """
        Initializes webdriver and configures several options specific to walmart scrapping.
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        options.add_argument('--headless')
        options.add_argument('--disable-extensions')
        options.add_argument('disable-infobars')

        driver = webdriver.Chrome(executable_path=settings.CHROME_DRIVER_EXECUTABLE, chrome_options=options)
        driver.get(self.product_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        self.parse_page_content(soup)
        return self.__dict__


class WalmartScrapper:
    """
    Responsible for scrapping walmart data.
    """
    def __init__(self, url):
        self.product_url = url
        self.product_name = None
        self.product_price = None
        self.product_review_score = None
        self.product_availability = 'Available'

    def parse_page_content(self, soup):
        try:
            self.product_name = soup.find('h1', {"itemprop": "name"}).get_text().strip()
        except Exception as e:
            self.product_name = 'BAD REQUEST'
        try:
            self.product_price = soup.find('span', {"itemprop" : "price"})
            self.product_price = float(self.product_price.get_text().replace('$', '').replace(',', '').strip())
        except Exception as e:
            self.product_price = 'BAD REQUEST'
        try:
            self.product_review_score = soup.find('span', {"class" : "f7 rating-number"}).get_text() + ' out of 5 stars'
        except Exception as e:
            self.product_review_score = 'BAD REQUEST'

    def fetch_product_details(self):
        """
        Initializes webdriver and configures several options specific to walmart scrapping.
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        options.add_argument('--headless')
        options.add_argument('--disable-extensions')
        options.add_argument('disable-infobars')

        driver = webdriver.Chrome(executable_path=settings.CHROME_DRIVER_EXECUTABLE, chrome_options=options)
        driver.get(self.product_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        self.parse_page_content(soup)
        return self.__dict__


class TargetScrapper:
    """
    Responsible for scrapping Target data.
    """
    def __init__(self, url):
        self.product_url = url
        self.product_name = None
        self.product_price = None
        self.product_review_score = None
        self.product_availability = None

    def parse_page_content(self, soup):
        try:
            self.product_name = soup.find('span', {"itemprop": "name"}).get_text().strip()
        except Exception as e:
            self.product_name = 'BAD REQUEST'
        try:
            self.product_price = soup.find('div', {"data-test" : "product-price"})
            self.product_price = float(self.product_price.get_text().replace('$', '').replace(',', '').strip())
        except Exception as e:
            self.product_price = 'BAD REQUEST'
        try:
            self.product_review_score = soup.find('h2', {"data-test" : "ratingCountText"}).get_text() + ' out of 5 stars'
        except Exception as e:
            self.product_review_score = 'BAD REQUEST'

    def fetch_product_details(self):
        """
        Initializes webdriver and configures several options specific to Target scrapping.
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        options.add_argument('--headless')
        options.add_argument('--disable-extensions')
        options.add_argument('disable-infobars')

        driver = webdriver.Chrome(chrome_options=options)
        driver.get(self.product_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        self.parse_page_content(soup)
        return self.__dict__


class CostcoScrapper:
    """
    Responsible for scrapping Costco data.
    """
    def __init__(self, url):
        self.product_url = url
        self.product_name = None
        self.product_price = None
        self.product_review_score = None
        self.product_availability = None

    def parse_page_content(self, soup):
        try:
            self.product_name = soup.find('span', {"itemprop": "name"}).get_text().strip()
        except Exception as e:
            self.product_name = 'BAD REQUEST'
        try:
            self.product_price = float(soup.find('span', {"automation-id": "productPriceOutput"}).strip())
        except Exception as e:
            self.product_price = 'BAD REQUEST'
        try:
            self.product_review_score = soup.find('span', {"itemprop" : "ratingValue"}).get_text().strip()
        except Exception as e:
            self.product_review_score = 'BAD REQUEST'

    def fetch_product_details(self):
        """
        Initializes webdriver and configures several options specific to Costco scrapping.
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        options.add_argument('--headless')
        options.add_argument('--disable-extensions')
        options.add_argument('disable-infobars')

        driver = webdriver.Chrome(chrome_options=options)
        driver.get(self.product_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        self.parse_page_content(soup)
        return self.__dict__

