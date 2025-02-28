from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from core.utils import open_data_file

url = "https://bulbapedia.bulbagarden.net/wiki/List_of_moves"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

with open_data_file("pokemon_moves") as f:
    f.write(f"# {url}\n")
    for tr in soup.select("div#mw-content-text table table tr"):
        if tr.find().name == "th":
            continue
        a = tr.find("a")
        f.write(f"[{a.string}](<{urljoin(url, a['href'])}>)\n")
