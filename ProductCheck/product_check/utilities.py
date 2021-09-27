from django.core.mail import EmailMultiAlternatives, BadHeaderError
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from smtplib import SMTPException


def mail_user(product_data):
    """
    Utility function used to update customer regarding the price change via mail.

    Args:
    product_data: Latest scrapped product data.

    Returns:
        Scraped data and success http code.

    Raises:
        BadHeaderError: Raises an exception to prevent header injection.
        SMTPException: Handles all smtplib exceptions.
        Exception: Raises an exception.
    """
    try:
        subject = 'ProductCheck price alert'
        from_email = settings.DEFAULT_FROM
        to_email = settings.DEFAULT_TO

        html_content = render_to_string('mail_template.html', {'product_url': product_data['product_url'], 'price': product_data['product_price']})
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    except BadHeaderError as error:
        print('Subject was not properly formatted' + str(error))
    except SMTPException as error:
        print('There was an error sending an email.' + str(error))
    except Exception as error:
        print('There was an error sending an email.' + str(error))
