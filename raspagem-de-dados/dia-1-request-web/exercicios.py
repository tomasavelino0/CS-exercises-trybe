from parsel import Selector
import requests

URL = "http://books.toscrape.com/catalogue/the-grand-design_405/index.html"


response = requests.get(URL)
selector = Selector(text=response.text)

title = selector.css("div.product_main > h1::text").get()
price = selector.css("div.product_main > p.price_color::text").re_first(
    r"\d+\.\d{2}"
)

suffix = "...more"
description = selector.css("article.product_page > p::text").get()
if description.endswith(suffix):
    description.replace(suffix, " ")

image = selector.css("div.active > img::attr(src)").get()
url_image = "http://books.toscrape.com/catalogue/" + image

info_book = f"{title}, {price}, {description}, {url_image}"
print(info_book)
