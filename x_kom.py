import os
import smtplib
import ssl
from requests_html import HTMLSession

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USER = os.environ['EMAIL_USER']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
RECEIVER_EMAIL = os.environ['RECEIVER_EMAIL']
URL = 'https://www.x-kom.pl/goracy_strzal'


def get_data_send_email():
    session = HTMLSession()
    r = session.get(URL)

    product_name = r.html.find('.sc-1x6crnh-5', first=True)
    old_price = r.html.find('.sc-8c7p9j-3', first=True)
    new_price = r.html.find('.sc-8c7p9j-2', first=True)

    message = f"""\
    Subject: {product_name.text} from {old_price.text} to {new_price.text}
    
    {URL}
    """.encode('utf-8')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', EMAIL_PORT, context=context) as server:
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, RECEIVER_EMAIL, message)


if __name__ == '__main__':
    get_data_send_email()
