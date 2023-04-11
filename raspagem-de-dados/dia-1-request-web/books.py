from parsel import Selector
import requests


response = requests.get("http://books.toscrape.com/")
selector = Selector(text=response.text)
quotes = []
precos = selector.css("div.product_price > p.price_color::text").re(
    r"£\d+\.\d{2}"
)
livros = selector.css("article.product_pod > h3 > a::attr(title)").getall()
for index, livro in enumerate(livros):
    quotes.append(
        {"titulo": livro, "price": precos[index]},
    )
    formatar = quotes[index]["price"]
print(quotes[0])
