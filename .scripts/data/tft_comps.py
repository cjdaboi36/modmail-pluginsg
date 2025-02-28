import requests
from core.utils import open_data_file

url = "https://tftacademy.com/api/tierlist/comps"
r = requests.get(url)
data = r.json()

with open_data_file("tft_comps") as f:
    f.write(f"# {url}\n")
    for guide in data["guides"]:
        if guide["isPublic"]:
            print(guide)
            f.write(
                f"[{guide['title']}](<https://tftacademy.com/tierlist/comps/{guide['compSlug']}>)\n"
            )
