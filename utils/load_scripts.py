from pathlib import Path


def load_collection():
    data = ""
    path = Path(__file__).parent / "../data/scripts/collection.js"

    with open(path, "r") as file:
        data = file.read()

    return data
