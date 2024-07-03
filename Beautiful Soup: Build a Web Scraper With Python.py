# if you get this error : "AttributeError: 'NoneType' object has no attribute 'get_text'" keep refresh the code till it works
import requests
from bs4 import BeautifulSoup
import lxml

URL= "https://www.amazon.com.au/gp/product/B09QT8YRKH/ref=ox_sc_saved_image_1?smid=A3T0EB8OL2A6FL&th=1"
# your headers from https://myhttpheader.com/
HEADERS = {
    'Accept-Language': "en-GB,en-US;q=0.9,en;q=0.8",
    'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}
response = requests.get(url=URL, headers=HEADERS)
# website_html = response.text
website_html = response.content
soup = BeautifulSoup(website_html,"lxml")

price = soup.find(class_="a-offscreen").get_text()
print(price)
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

import smtplib

my_email = "kia.sydney@gmail.com"
password = "dpclsiumypmeacsy"
title = soup.find(id="productTitle").get_text()
print(title)
BUY_PRICE = 200


link_to_buy = "https://www.amazon.com.au/gp/product/B09QT8YRKH/ref=ox_sc_saved_image_1?smid=A3T0EB8OL2A6FL&th=1"

if price_as_float < BUY_PRICE:
    message = (f"{title} is now {price}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="kiano.keynejad@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\nurl:{link_to_buy}".encode("utf-8")
        )


