from pathlib import Path
from decouple import config

API_HOSTNAME = config("API_HOSTNAME")


def load_collection():
    data = ""
    path = Path(__file__).parent / "../data/scripts/collection.js"

    with open(path, "r") as file:
        data = file.read()

    data = data.replace("<API_HOSTNAME>", API_HOSTNAME)

    return data
