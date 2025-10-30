import os
from typing import TextIO

HEADERS = {
    "User-Agent": "modmail-plugins/1.0 (https://github.com/RealCyGuy/modmail-plugins)",
}


def open_data_file(name: str) -> TextIO:
    return open(
        os.path.join("..", "..", "clickthebutton", "data", name + ".txt"),
        "w",
        encoding="utf-8",
    )


def contains_swear(text: str) -> bool:
    return any(word in text for word in ["fuck", "bitch", "dick", "sex"])
