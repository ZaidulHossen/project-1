from bs4 import BeautifulSoup
import requests
url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.select("span.text")
c=1
for i in quotes:
    print(f"{c}. {i.get_text()}")
    c = c + 1