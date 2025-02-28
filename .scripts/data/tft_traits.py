from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from core.utils import open_data_file

url = "https://wiki.leagueoflegends.com/en-us/Category:TFT_traits"


with open_data_file("tft_traits") as f:
    f.write(f"# {url}\n")
    while url:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        category = soup.find("div", {"id": "mw-pages"}).find(
            "div", {"class": "mw-content-ltr"}
        )
        for a in category.select("a"):
            if a.get("href") and a.string:
                f.write(f"[{a.string[4:]}](<{urljoin(url, a['href'])}>)\n")
        next_page = category.parent.find("a", string="next page")
        if next_page:
            url = urljoin(url, next_page["href"])
        else:
            url = None
