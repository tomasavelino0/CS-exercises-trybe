import requests
from bs4 import BeautifulSoup


def get_content_html(url):
    page = requests.get(url)
    content = page.text
    soup = BeautifulSoup(content, "html.parser")
    soup.prettify()
    return soup


# content = get_content_html("https://quotes.toscrape.com/")
# citacoes = content.find("span", "text").string

# print(citacoes)

# content2 = get_content_html(
#     "https://www.wikimetal.com.br/iron-maiden-scorpions-kiss-veja-melhores-albuns-1982"
# )

# paragrafos = content2.find("div", {"class": "entry-content"}).find_all("p")
# print(paragrafos)

content3 = get_content_html("https://pt.wikipedia.org/wiki/Rock_in_Rio%22")

all_href = [
    anchor["href"]
    for anchor in content3.find_all("a")
    if anchor.get("href") is not None
]

print(all_href)
