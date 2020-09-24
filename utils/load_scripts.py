from os import environ
from pathlib import Path


def load_collection(API_HOSTNAME, ENV):
    path = Path(__file__).parent / "../data/scripts/collection.js"

    with open(path, "r") as file:
        data = file.read()

    data = data.replace("<API_HOSTNAME>", API_HOSTNAME)

    if ENV == "PRODUCTION":
        data = data.replace("http://", "https://")

    return data
