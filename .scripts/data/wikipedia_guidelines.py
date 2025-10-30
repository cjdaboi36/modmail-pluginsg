import re

import requests
from core.utils import HEADERS, open_data_file

url = "https://en.wikipedia.org/wiki/Wikipedia:Shortcut_index?action=raw"
r = requests.get(url, headers=HEADERS)

with open_data_file("wikipedia_guidelines") as f:
    f.write(f"# {url}\n")

    in_target_section = False

    for line in r.text.splitlines():
        line = line.strip()

        if line == "== Procedures, policies, and guidelines ==":
            in_target_section = True
            continue

        if in_target_section and line.startswith("== "):
            in_target_section = False

        if not in_target_section:
            continue

        if line.startswith("| style"):
            parts = line.split("|")
            matches = re.findall(r"\[\[(WP:[^\]]+)\]\]", parts[-1])

            for match in matches:
                f.write(f"{match} \n")
