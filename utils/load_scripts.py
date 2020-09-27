from os import environ
from pathlib import Path


def load_collection(TRACK_HOSTNAME, ENV):
    path = Path(__file__).parent / "../data/scripts/collection.js"

    with open(path, "r") as file:
        data = file.read()

    data = data.replace("<TRACK_HOSTNAME>", TRACK_HOSTNAME)

    if ENV == "PRODUCTION":
        data = data.replace("http://", "https://")

    return data
