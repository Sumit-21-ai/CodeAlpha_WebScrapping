import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []

for q in soup.find_all("span", class_="text"):
    quotes.append(q.text)

df = pd.DataFrame(quotes, columns=["Quotes"])
print(df)

df.to_csv("quotes.csv", index=False)