import requests
import bs4

URL = "https://www.jpx.co.jp/markets/derivatives/settlement-price/index.html"

resp = requests.get(URL)
resp.raise_for_status()
soup = bs4.BeautifulSoup(resp.text, "html.parser")
a_tags = soup.find_all("a")
for a_tag in a_tags:
    link = a_tag.get("href")
    if link.endswith(".csv"):
        url = "https://www.jpx.co.jp" + link
        resp = requests.get(url)
        resp.raise_for_status()
        with open("option_list.csv", "wb") as f:
            f.write(resp.content)
