from .models import Product
from .views import scraping_class
from .utilities import mail_user


def periodic_product_scraping():
    """
    Cron job responsible for periodic scrapping of active product records stored in database.
    Notifies user regarding the price drop via mail.

    Raises:
        Exception: Raises an exception.
    """
    try:
        product_list = Product.objects.filter(is_active=True)
        for product in product_list:
            scrapper = scraping_class[product.product_category](product.product_url)
            scrapped_data = scrapper.fetch_product_details()
            if scrapped_data.get('product_price'):
                if scrapped_data['product_price'] < product.product_price:
                    mail_user(scrapped_data)
                product.product_price = scrapped_data.get('product_price')
                product.product_review_score = scrapped_data['product_review_score']
                product.product_availability = scrapped_data['product_availability']
                product.save()
    except Exception as e:
        raise e


def test_cron():
    """
    Test cron to ensure that crontab is configured properly.
    """
    print('This is to test the crontab configuration')
